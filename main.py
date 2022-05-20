from socketserver import TCPServer, BaseRequestHandler;

class TCPRequestHandler(BaseRequestHandler):
    def setup(self):
        self.file = open(".log", mode = "a", encoding = "utf-8")

    def handle(self):
        number, channel_id, time, group = self.request.recv(32).decode("utf-8").strip().replace("[CR]", "").split()
        
        if group == "00":
            print("спортсмен, нагрудный номер {0} прошел отсечку {1} в {2}".format(number, channel_id, time[:-2]))
        else:
            print("{0}: спортсмен, нагрудный номер {1} прошел отсечку {2} в {3}".format(group, number, channel_id, time), file = self.file)

if __name__ == "__main__":
    with TCPServer(("", 0), TCPRequestHandler) as server:
        print("Server running at: {}\n".format(server.server_address))
        server.serve_forever()
