from teide_node import MikNode


def send_show_command(node: MikNode, cmd: str) -> str:
    return node.send_raw_command(cmd)


def show_version(node: MikNode) -> str:
    cmd = "/system/routerboard/print"
    result = send_show_command(node, cmd)
    return result


def set_intf_description(node: MikNode, intf: str, description: str) -> str:
    cmd = f"/interface ethernet set [ find default-name={intf} ] comment={description}"
    result = send_show_command(node, cmd)
    return result
