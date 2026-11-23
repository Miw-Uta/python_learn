import socket
if __name__ == "__main__":
    # 1. 编写一个tcp 服务端程序
    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    tcp_server_socket.bind(("", 8080))
    # 设置监听
    tcp_server_socket.listen(128)

    while True:
        # 2. 获取浏览器发送的http 请求报文数据
        # 建立连接
        client_socket, client_addr = tcp_server_socket.accept()
        # 获取浏览器的请求信息
        client_request_data = client_socket.recv(1024).decode()
        print(client_request_data)
        # 3. 读取固定页面数据，把页面数据组装成 http 响应报文数据发送给浏览器
        with open("./../projects/to_do_list/index.html", "rb") as f:
            html_data = f.read()

        # 应答行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 应答头
        response_header = "Server: Python20WS/2.0\r\n"
        # 空行
        response_blank_line = "\r\n"
        # 应答体
        response_body = html_data 
        # 组装应答报文数据
        response_data = (response_line + response_header + response_blank_line).encode() + response_body
        # 发送应答报文数据给浏览器
        client_socket.send(response_data)

        # 4. http 响应报文数据发送完成以后，关闭服务于客户端的套接字
        client_socket.close()
