# Setting up an SSH connection to the container

The following python code could be used to SSH into a Docker container, and execute remotely a set of commands, and retrieve the results. 

For this trail setup I used the `paramiko` library for managing SSH sessions. See here for the 
[paramiko documentation](https://www.paramiko.org/)

After some initial testing I realized that this strategy (i.e. using SSH to interact with my Morpheus docker) was not an ideal solution for my setup (esp. since it added another layer of complexity). My testcode (which is pretty rudementary) is still placed in this repository to allow other to jumpstart from it if their setup might requires SSH access.


```python
# Import required libraries
import paramiko

# Function to establish SSH connection
def ssh_login(host, port, username, password):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        # Automatically add host keys if missing
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to the host
        ssh.connect(hostname=host, port=port, username=username, password=password)
        print(f"Connected to {host}")
        return ssh
    except Exception as e:
        print(f"Error connecting to {host}: {e}")
        return None

# Function to execute commands
def execute_commands(ssh, commands):
    outputs = {}
    for command in commands:
        try:
            print(f"Executing: {command}")
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode('utf-8').strip()
            error = stderr.read().decode('utf-8').strip()
            outputs[command] = {'output': output, 'error': error}
        except Exception as e:
            outputs[command] = {'output': '', 'error': str(e)}
    return outputs

# Function to close SSH connection
def close_ssh_connection(ssh):
    if ssh:
        ssh.close()
        print("SSH connection closed.")

# Main routine
if __name__ == "__main__":
    # SSH details
    host = "192.168.XXX.YYY"  # Replace with the container's IP
    port = 2222  # Replace with the container's SSH port
    username = "your_username"  # Replace with the container's username
    password = "your_password"  # Replace with the container's password

    # Some command to execute (just a few examples to test the connection)
    commands = [
        "ls -la",  # List all the files in the current directory
        "whoami"   # Check the current user's handle
    ]

    # Establish the SSH connection
    ssh = ssh_login(host, port, username, password)
    if ssh:
        # Execute commands and collect outputs
        results = execute_commands(ssh, commands)
        
        # Print outputs
        for command, result in results.items():
            print(f"Command: {command}")
            print(f"Output:\n{result['output']}")
            if result['error']:
                print(f"Error:\n{result['error']}")
            print("-" * 50)
        
        # Close SSH connection
        close_ssh_connection(ssh)
```

# Some important remarks

The code above comes without any warenty or fitness for purpose, as is very basic and should only be tried in your local environment. For instance, note that the code uses paramiko.AutoAddPolicy() to automatically add host keys if missing. This can pose a security risk, possibly making your connection vulnerable to man-in-the-middle attacks. Furthermore while the code does catch some of the exceptions, it does not provide detailed error messages. You could consider logging or printing more informative error messages to facilitate debugging (see [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)).


