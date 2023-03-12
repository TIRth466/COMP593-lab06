import requests
import hashlib
import os
import subprocess
def main():
  

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():

    # Set the URL for the text file that contains the hash value

    url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'

    # Send a GET request to the URL and retrieve the response
    response = requests.get(url)

    if response.status_code==requests.codes.ok:
        file_content=response.content
        


    # Extract the SHA-256 hash value from the response message body
      #  expected_hash = response.text.split()[0]

    #Download the latest VLC installer appropriate for the current system
    #installer_data=requests.get(url).content

    # Verify the integrity of the downloaded installer by comparing its SHA-256 hash value to the expected value
    #actual_hash = hashlib.sha256(installer_data).hexdigest()

    if response:
    # Save the installer file to disk if its integrity is verified
        with open('C:\github\COMP593-lab06\hash.txt', 'wb') as f:
            f.write(file_content)
            print('Installer saved to disk.')
    #Run the installer
        #os.system('C:\github\COMP593-lab06\hash.txt')
    else:
        print('Hash value mismatch. Installer not saved to disk.')



        

def download_installer():
    url='http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'

    response=requests.get(url)


    if response.status_code == requests.codes.ok:

        return response

def installer_ok(installer_data, expected_sha256):
    installer_data=hashlib.sha256(installer_data.content).hexdigest()

    if installer_data==expected_sha256:
        return f'file has been verified.'
    else:
        return f'infected with some malware.'

    
    
    
def save_installer(installer_data):
    temp_folder = os.getenv('TEMP')
    installer_path = os.path.join(temp_folder,'vlc-3.0.17.4-win64.exe') 
    with open(installer_path, 'wb') as f:
        f.write(installer_path)
    print('Installer saved to:', installer_path)
    # Run the installer
    #os.system(installer_path)
    
    

    

    return

def run_installer(installer_path):
    
    installer_path = os.path.join(installer_path)


# Run the installer using the subprocess module
    subprocess.run([installer_path,'/L=1033','/S'], check=True)

    return
    
def delete_installer(installer_path):
    installer_path=os.path.join(installer_path)
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()