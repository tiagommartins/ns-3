import ns.applications
import ns.core
import ns.visualizer
import ns.internet
import ns.network
import ns.point_to_point
import ns.csma
import sys

def configureTrace():
    ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
    ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)
    pass

def configureGatewayNodes():
    clientNodes = ns.network.NodeContainer()
    clientNodes.Create(2)
    return clientNodes

def configureGatewayDevices(gatewayNodes):
    pointToPoint = ns.point_to_point.PointToPointHelper()
    pointToPoint.SetDeviceAttribute("DataRate", ns.core.StringValue("100Mbps"))
    pointToPoint.SetChannelAttribute("Delay", ns.core.StringValue("200ms"))
    return pointToPoint.Install(gatewayNodes)

def configureCSMANodes(gatewayNode, replicas):
    csmaNodes = ns.network.NodeContainer()
    csmaNodes.Add(gatewayNode)
    csmaNodes.Create(replicas)
    return csmaNodes

def configureClientNodes(gatewayNode):
    return configureCSMANodes(gatewayNode, 6)

def configureServerNodes(gatewayNode):
    return configureCSMANodes(gatewayNode, 3)

def configureCSMADevices(csmaNodes):
    csma = ns.csma.CsmaHelper()
    csma.SetChannelAttribute("DataRate", ns.core.StringValue("1Gbps"))
    csma.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))
    return csma.Install(csmaNodes)

def configureInternetStack(serverNodes, clientNode):
    stack = ns.internet.InternetStackHelper()
    stack.Install(serverNodes)
    stack.Install(clientNode)
    pass

def configureAddress(address, devices, ipv4Address) :
    address.SetBase(ns.network.Ipv4Address(ipv4Address), ns.network.Ipv4Mask("255.255.255.0"))
    return address.Assign(devices)

def configureAddressClient(address, clientDevices) :
    return configureAddress(address, clientDevices, "10.1.1.0")

def configureAddressServer(address, serverDevices) :
    return configureAddress(address, serverDevices, "10.1.2.0")

def configureAddressGateway(address, gatewayDevices) :
    return configureAddress(address, gatewayDevices, "10.1.3.0")

def configureAppServer(serverNode):
    echoServer = ns.applications.UdpEchoServerHelper(9)
    serverApps = echoServer.Install(serverNode)
    serverApps.Start(ns.core.Seconds(1.0))
    serverApps.Stop(ns.core.Seconds(11.0))
    pass

def configureAppClient(clientNode, serverTarget, interval):
    echoClient = ns.applications.UdpEchoClientHelper(serverTarget, 9)
    echoClient.SetAttribute("MaxPackets", ns.core.UintegerValue(10000))
    echoClient.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds(interval)))
    echoClient.SetAttribute("PacketSize", ns.core.UintegerValue(1024))
    clientApps = echoClient.Install(clientNode)
    clientApps.Start(ns.core.Seconds(2.0))
    clientApps.Stop(ns.core.Seconds(10.0))
    pass

cmd = ns.core.CommandLine()
cmd.Parse(sys.argv)

configureTrace()

gatewayNodes = configureGatewayNodes()
gatewayDevices = configureGatewayDevices(gatewayNodes)

clientNodes = configureClientNodes(gatewayNodes.Get(0))
clientDevices = configureCSMADevices(clientNodes)

serverNodes = configureServerNodes(gatewayNodes.Get(1))
serverDevices = configureCSMADevices(serverNodes)

configureInternetStack(serverNodes, clientNodes)

address = ns.internet.Ipv4AddressHelper()
configureAddressGateway(address, gatewayDevices)
configureAddressClient(address, clientDevices)
serverInterfaces = configureAddressServer(address, serverDevices)

configureAppServer(serverNodes.Get(1))
configureAppServer(serverNodes.Get(2))
configureAppServer(serverNodes.Get(3))

configureAppClient(clientNodes.Get(1), serverInterfaces.GetAddress(3), 0.20)
configureAppClient(clientNodes.Get(2), serverInterfaces.GetAddress(2), 0.33)
configureAppClient(clientNodes.Get(3), serverInterfaces.GetAddress(1), 0.46)
configureAppClient(clientNodes.Get(4), serverInterfaces.GetAddress(3), 0.59)
configureAppClient(clientNodes.Get(5), serverInterfaces.GetAddress(2), 0.72)
configureAppClient(clientNodes.Get(6), serverInterfaces.GetAddress(1), 0.85)

ns.internet.Ipv4GlobalRoutingHelper.PopulateRoutingTables()

ns.core.Simulator.Stop(ns.core.Seconds(11.0))

ns.core.Simulator.Run()
ns.core.Simulator.Destroy()