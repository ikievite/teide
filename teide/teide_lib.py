# from teide.teide_node import MikNode


def send_show_command(node, cmd: str) -> str:
    return node.send_raw_command(cmd)


def add_user(node, user_name: str, group: str, password: str) -> str:
    cmd = f"/user add group={group} name={user_name} password={password}"
    result = send_show_command(node, cmd)
    return result


def change_user_password(node, user_name: str, password: str) -> str:
    cmd = f"/user set {user_name} password={password}"
    result = send_show_command(node, cmd)
    return result


def create_user_group(node, group_name: str, policies: list) -> str:
    policies = ",".join(policies)
    cmd = f"/user group/add name={group_name} policy={policies}"
    result = send_show_command(node, cmd)
    return result


def show_ip_address(node) -> str:
    cmd = "/ip/address/print"
    result = send_show_command(node, cmd)
    return result


def show_version(node) -> str:
    cmd = "/system/routerboard/print"
    result = send_show_command(node, cmd)
    return result


def set_intf_description(node, intf: str, description: str) -> str:
    cmd = f"/interface ethernet set [ find default-name={intf} ] comment={description}"
    result = send_show_command(node, cmd)
    return result
