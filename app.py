# app.py
from flask import Flask, render_template, request, jsonify, send_file
import random
import string
import re
import os

app = Flask(__name__)

def generate_usernames(num_users, char_set):
    """
    Generate random usernames based on user specifications.
    
    :param num_users: Number of usernames to generate
    :param char_set: Character set to use (lowercase, uppercase, or mixed)
    :return: List of generated usernames
    """
    usernames = []
    
    # Define character sets
    if char_set == 'lowercase':
        chars = string.ascii_lowercase
    elif char_set == 'uppercase':
        chars = string.ascii_uppercase
    else:  # mixed case
        chars = string.ascii_letters
    
    for _ in range(num_users):
        # Generate username length between 6-12 characters
        username_length = random.randint(6, 12)
        
        # Generate username with random characters
        username = ''.join(random.choice(chars) for _ in range(username_length))
        
        # Optional: Add a random number to make usernames more unique
        if random.random() > 0.5:
            username += str(random.randint(10, 999))
        
        usernames.append(username)
    
    return usernames

def update_config_file(new_usernames):
    """
    Update the config.cfg file with new usernames while preserving file structure.
    
    :param new_usernames: List of new usernames to append
    :return: Path to the updated config file
    """
    config_path = 'config.cfg'
    
    # Read the entire file content
    with open(config_path, 'r') as file:
        content = file.read()
    
    # Find the users section
    users_match = re.search(r'users:\n(.*?)(\n\n|$)', content, re.DOTALL)
    
    if users_match:
        # Get existing users
        existing_users_block = users_match.group(1)
        existing_users = [line.strip().lstrip('- ') for line in existing_users_block.split('\n') if line.strip().startswith('- ')]
        
        # Add new usernames, avoiding duplicates
        for username in new_usernames:
            if username not in existing_users:
                existing_users.append(username)
        
        # Recreate the users block
        new_users_block = '\n'.join([f'  - {user}' for user in existing_users])
        
        # Replace the old users block with the new one
        updated_content = content[:users_match.start(1)] + new_users_block + content[users_match.end(1):]
        
        # Write back to the file
        with open(config_path, 'w') as file:
            file.write(updated_content)
    
    return config_path

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate usernames based on form input"""
    num_users = int(request.form.get('numUsers', 5))
    char_set = request.form.get('charSet', 'mixed')
    
    # Validate input
    num_users = max(1, min(num_users, 20))  # Ensure between 1-20
    
    # Generate usernames
    usernames = generate_usernames(num_users, char_set)
    
    # Update config file with new usernames
    update_config_file(usernames)
    
    return jsonify(usernames)

@app.route('/download')
def download_config():
    """Download the updated config file"""
    config_path = 'config.cfg'
    return send_file(config_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)