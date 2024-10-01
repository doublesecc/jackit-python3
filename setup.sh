#!/usr/bin/env bash

main(){
    echo -e '\n[~] It is recommended to run this script with the following command:'
    echo -e 'source ./setup.sh\n'

    echo "[?] Do you want to continue executing this script? [y/N]" 
    read response
    case "$response" in
        [yY][eE][sS]|[yY])
        true
        ;;
    *)
            echo -e '\n[!] Exiting, please this script again with the following command:'
            echo -e 'source ./setup.sh\n'
            return 0
            ;;
    esac

    echo -e '\n[~] Checking that this script is being ran as sudo user\n'
    sudo id &>/dev/null
            if [ "$?" -eq 0 ]
            then
              # Just continue through script
              true
            else
              echo -e "\n[!] - You cannot run sudo commands!\nExiting"
              return 0
            fi

    echo -e '\n[~] Installing python3 system packages\n'
    sudo apt -qq install python3 python3-pip python3-venv python3-usb -y
    echo -e '\n[+] python3 system packages installed'

    echo -e '\n[~] Setting up python3 venv for jackit'
    mkdir -p ~/venv
    python3 -m venv ~/venv/jackit
    source ~/venv/jackit/bin/activate
    echo -e '[+] jackit venv created and activated'

    echo -e '\n[~] Installing required pip3 packages'
    pip3 install -q -r requirements.txt
    echo -e '[+] python3 pip packages installed'

    echo -e '\n[~] Installing python package for jackit'
    pip3 install -q -e .
    echo -e '[+] jackit pip package installed'

    echo -e '\n[+] Setup complete!\n'
    echo -e '[~] You can exit the venv with the following command:'
    echo -e 'deactivate'

    echo -e '\n[~] You should be able to use jackit with the following command:'
    echo -e 'sudo ~/venv/jackit/bin/jackit\n'
}

main "$@";
