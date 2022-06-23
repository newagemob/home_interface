'''
list of commands that can be used to control nodes throughout the network
'''

import tkinter as tk

# for every print statement, output the text to tkinter text box
class cmdIndex:
    def __init__(self):
        self.cmds = {
            'help': self.help,
            'add': self.add,
            'remove': self.remove,
            'connect': self.connect,
            'disconnect': self.disconnect,
            'ping': self.ping,
            'exit': self.exit,
            'lights': self.lights,
            'cameras': self.cameras,
            'appliances': self.appliances,
            'humidity': self.humidity,
            'temperature': self.temperature,
            'doors': self.doors,
            'windows': self.windows,
            'switches': self.switches,
            'irrigation': self.irrigation,
            'all': self.all,
            'log': self.log,
            'errorLog': self.errorLog
        }

    def help(self, *args):
      if len(args) == 0:
        print("help: list all commands")
        # Node Manager Commands
        print("add: add a node")
        print("remove: remove a node")
        print("connect: connect two nodes")
        print("disconnect: disconnect two nodes")
        print("ping: ping a node")
        # System Commands
        print("exit: exit the program")
        # Interface Commands
        print("lights: list all lights nodes")
        print("cameras: list all cameras nodes")
        print("appliances: list all appliance nodes")
        print("humidity: list all humidity nodes")
        print("temperature: list all temperature nodes")
        print("doors: list all door nodes")
        print("windows: list all window nodes")
        print("switches: list all switch nodes")
        print("irrigation: list all irrigation nodes")
        print("all: list all nodes")
        # Errors
        print("log: print system logs")
        print("errorLog: print error logs")
        print("usage: help <command>")
        print("command: help, add, remove, connect, disconnect, ping, exit, lights, cameras, appliances, humidity, temperature, doors, windows, switches, irrigation, all, log, errorLog")
      else:
        print("usage: help <command>")
        print("command: help, add, remove, connect, disconnect, ping, exit, lights, cameras, appliances, humidity, temperature, doors, windows, switches, irrigation, all, log, errorLog")
      
    def getCmd(self, cmd): # returns the function associated with the command
        if cmd in self.cmds:
            return self.cmds[cmd]
        else:
            return self.error

    def add(self, *args):
      if args == None:
        print("add: add a node")
        print("Usage: add <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")
      else:
        print("usage: add <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")

    def remove(self, *args):
      if len(args) == 0:
        print("remove: remove a node")
        print("Usage: remove <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")
      else:
        print("usage: remove <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")

    def connect(self, *args):
      if len(args) == 0:
        print("connect: connect a node to the network")
        print("Usage: connect <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")
      else:
        print("usage: connect <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")

    def disconnect(self, *args):
      if len(args) == 0:
        print("disconnect: disconnect a node from the network")
        print("Usage: disconnect <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")
      else:
        print("usage: disconnect <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")

    def ping(self, *args):
      if len(args) == 0:
        print("ping: ping a node")
        print("Usage: ping <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")
      else:
        print("usage: ping <node_type> <node_name>")
        print("node_type: lights, cameras, appliance, humidity, temperature, door, window, switch, irrigation")

    def exit(self):
        exit = input("Are you sure you want to exit? (y/n)")
        if exit == 'y':
            print("Exiting...")
            quit()
        else:
            print("Exiting aborted")
            pass

    def lights(self, *args):
      if len(args) == 0:
        print("lights: list all lights nodes")
        print("Usage: lights <node_name> <function>")
        print("node_name: name of the lights node")
        print("function: on, off, toggle, history")
      else:
        print("usage: lights <node_name> <function>")
        print("node_name: name of the lights node")
        print("function: on, off, toggle, history")

    def cameras(self, *args):
      if len(args) == 0:
        print("cameras: list all cameras nodes")
        print("Usage: cameras <node_name> <function>")
        print("node_name: name of the cameras node")
        print("function: on, off, toggle, accessLive, accessStorage")
      else:
        print("usage: cameras <node_name> <function>")
        print("node_name: name of the cameras node")
        print("function: on, off, toggle, accessLive, accessStorage")

    def appliances(self, *args):
      if len(args) == 0:
        print("appliances: list all appliance nodes")
        print("Usage: appliances <node_name> <function>")
        print("node_name: name of the appliance node")
        print("function: on, off, toggle, history")
      else:
        print("usage: appliances <node_name> <function>")
        print("node_name: name of the appliance node")
        print("function: on, off, toggle, history")

    def humidity(self, *args):
      if len(args) == 0:
        print("humidity: list all humidity nodes")
        print("Usage: humidity <node_name> <function>")
        print("node_name: name of the humidity node")
        print("function: current, history")
      else:
        print("usage: humidity <node_name> <function>")
        print("node_name: name of the humidity node")
        print("function: current, history")

    def temperature(self, *args):
      if len(args) == 0:
        print("temperature: list all temperature nodes")
        print("Usage: temperature <node_name> <function>")
        print("node_name: name of the temperature node")
        print("function: adjust <value>, current, history")
      else:
        print("usage: temperature <node_name> <function>")
        print("node_name: name of the temperature node")
        print("function: adjust <value>, current, history")

    def doors(self, *args):
      if len(args) == 0:
        print("doors: list all door nodes")
        print("Usage: doors <node_name> <function>")
        print("node_name: name of the door node")
        print("function: lock, unlock, history, current")
      else:
        print("usage: doors <node_name> <function>")
        print("node_name: name of the door node")
        print("function: lock, unlock, history, current")

    def windows(self, *args):
      if len(args) == 0:
        print("windows: list all window nodes")
        print("Usage: windows <node_name> <function>")
        print("node_name: name of the window node")
        print("function: open, close, history, current")
      else:
        print("usage: windows <node_name> <function>")
        print("node_name: name of the window node")
        print("function: open, close, history, current")

    def switches(self, *args):
      if len(args) == 0:
        print("switches: list all switch nodes")
        print("Usage: switches <node_name> <function>")
        print("node_name: name of the switch node")
        print("function: on, off, toggle, history")
      else:
        print("usage: switches <node_name> <function>")
        print("node_name: name of the switch node")
        print("function: on, off, toggle, history")

    def irrigation(self, *args):
      if len(args) == 0:
        print("irrigation: list all irrigation nodes")
        print("Usage: irrigation <node_name> <function>")
        print("node_name: name of the irrigation node")
        print("function: on, off, toggle, history")
      else:
        print("usage: irrigation <node_name> <function>")
        print("node_name: name of the irrigation node")
        print("function: on, off, toggle, history")

    def all(self):
        print("all: list all nodes")
        print("Usage: all")

    def log(self, *args):
      if len(args) == 0:
        print("log: print system logs")
        print("Usage: log")
      else:
        print("usage: log <node_name>")

    def errorLog(self, *args):
      if len(args) == None:
        print("errorLog: print error logs")
        print("Usage: errorLog")
      else:
        print("usage: errorLog <node_name>")

    cmds = {
        'help': help,
        'add': add,
        'remove': remove,
        'connect': connect,
        'disconnect': disconnect,
        'ping': ping,
        'exit': exit,
        'lights': lights,
        'cameras': cameras,
        'appliances': appliances,
        'humidity': humidity,
        'temperature': temperature,
        'doors': doors,
        'windows': windows,
        'switches': switches,
        'irrigation': irrigation,
        'all': all,
        'log': log,
        'errorLog': errorLog
    }

    # whatever function is called, store the printed output in a variable
