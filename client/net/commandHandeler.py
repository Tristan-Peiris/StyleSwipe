def uploadItem(client, item, name):
  print(item, name)
  print("sending request")
  client.send("upload clothing item".encode())
  print("sent request, wait for response...")
  if client.recv(1024).decode() == "ready":
      print("server is ready, sending item...")
      client.sendall(str(item).encode())
      client.send(name.encode())
      print("item sent, confirming success...")
      if client.recv(1024).decode() == "received":
          print("item received")
      else:
          print("error: server did not receive item")
          return "error"
  else:
      print("error: server is not ready")
      return "error"