import subprocess
import optparse
import re


def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest = 'interface', help = 'enter a interface')
    parser.add_option('-m', '--mac', dest = 'mac_address', help = 'enter a mac address')

    return parser.parse_args()

def change_mac_address(mac_address, interface):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
    subprocess.call(['ifconfig', interface, 'up'])

def check_new_mac(interface):
    ifconfig = subprocess.check_output(['ifconfig', interface])
    new_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig))

    if new_mac:
        return new_mac.group(0)


print('macchanger has been started')

(inputs, arguments) = get_inputs()
change_mac_address(inputs.mac_address, inputs.interface)
final_mac = check_new_mac(inputs.interface)

if inputs.mac_address == final_mac:
    print('success')
else:
    print('error')


