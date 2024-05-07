# MAC Address Changer

This Python script allows you to change the MAC address of a network interface in Linux.

## Prerequisites

- Python 3 installed on your system.
- You must have administrative privileges to run this script.
- Only works on Linux systems.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/mac-address-changer.git
    ```

2. **Navigate to the Directory**: Navigate to the directory containing the script.

    ```bash
    cd mac-address-changer
    ```

3. **Run the Script**: Run the script with administrative privileges and specify the interface and the new MAC address.

    ```bash
    sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
    ```

    Replace `<interface>` with the name of your network interface (e.g., eth0, wlan0) and `<new_mac_address>` with the desired MAC address.

    Example:

    ```bash
    sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
    ```

4. **Confirm Successful Change**: If the MAC address is changed successfully, you'll see a confirmation message.

## Disclaimer

Changing your MAC address may violate the terms of service of your network provider. Use this script responsibly and only on networks you are authorized to access.

## Support

For any issues or suggestions, please open an issue in the GitHub repository.
