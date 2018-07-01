import sys
import pexpect


if __name__=='__main__':

    # Validate that ip address is valid.
    ip_addr = sys.argv[1]
    ip_addr = ip_addr.strip()
    ip_addr = ip_addr.split(".")
    if not len(ip_addr) == 4:
        print("This is not a valid ip")
        exit()
    for octet in ip_addr:
        if octet == '':
            print("This is not a valid ip")
            exit()
        octet = int(octet)
        if not octet >=0 and not octet <= 255:
            print("This is not a valid ip")
            exit()
    valid_ip = ""
    for octet in ip_addr:
        valid_ip += str(octet) + "."
    valid_ip = valid_ip[:-1]
    print(valid_ip)


child = pexpect.spawn("ftp " + valid_ip)
child.expect("[Nn]ame .*:")
print(child.before)
print(child.after)
child.sendline("anonymous")
child.expect("[Pp]assword:")
print(child.after)
child.sendline(" ")
child.expect("ftp")
print(child.after)
child.sendline("ls")
child.expect("150")
child.interact()

