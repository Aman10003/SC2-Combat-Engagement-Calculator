import port

def test_open_port():
    open_ports = port.get_open_ports()
    assert len(open_ports) > 1

def test_find_unused_port():
    port_assignment = port.find_unused_port()
    assert port_assignment >= 8000 & port_assignment <= 9000