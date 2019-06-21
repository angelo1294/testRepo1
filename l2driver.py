def createVlan(vlanId=''):
	pass

def destroyVlan(vlanId=''):
	pass

def addToVlan(vlanId='', portNumber='', tagging='', *args):
	pass

def removeFromVlan(vlanId='', portNumber='', tagging='', *args):
	pass

def getPorts():
	returnJson = {"ports": []}
	return returnJson

def getProperties(args):
	returnJson = {"ports": [], "properties": {}}
	return returnJson

def connect(args):
	return "1"

def disconnect(args):
	return "1"

def getConnections():
	returnJson = {'connections': []}
	return returnJson
