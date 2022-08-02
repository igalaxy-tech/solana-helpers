inv = "sol{} ansible_host={} ansible_user=root ansible_python_interpreter=/usr/bin/python3 ansible_ssh_pass={}"
sol_number_list, sol_ip_list, sol_pass_list = [], [], []
f = open("raw", "r")
lines = f.readlines()
for line in lines:
    if line.strip():
        clear_line = []
        line_list = line.strip().split("\t")
        for i in line_list:
            i = i.strip()
            if i != "":
                clear_line.append(i)
        if clear_line[0] == "Client number":
            clear_line.pop(0)
            sol_number_list += clear_line
        if clear_line[0] == "Server":
            clear_line.pop(0)
            sol_ip_list += clear_line
        if clear_line[0] == "Server Password":
            clear_line.pop(0)
            sol_pass_list += clear_line

if len(sol_number_list) == len(sol_ip_list) == len(sol_pass_list):
    print('\n'.join(inv.format(num, ip, pwd) for num, ip, pwd in zip(sol_number_list, sol_ip_list, sol_pass_list)))
else:
    print("List len mismatch. ", len(sol_number_list), len(sol_ip_list), len(sol_pass_list))

