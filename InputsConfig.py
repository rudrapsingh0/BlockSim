
class InputsConfig:

    """ Seclect the model to be simulated.
    0 : The base model
    1 : Bitcoin model
    2 : Ethereum model
        3 : AppendableBlock model
    """
    model = 2

    ''' Input configurations for the base model '''
    if model == 0:

        ''' Block Parameters '''
        Binterval = 600  # Average time (in seconds)for creating a block in the blockchain
        Bsize = 1.0  # The block size in MB
        Bdelay = 0.42  # average block propogation delay in seconds, #Ref: https://bitslog.wordpress.com/2016/04/28/uncle-mining-an-ethereum-consensus-protocol-flaw/
        Breward = 12.5  # Reward for mining a block

        ''' Transaction Parameters '''
        hasTrans = True  # True/False to enable/disable transactions in the simulator
        Ttechnique = "Light"  # Full/Light to specify the way of modelling transactions
        Tn = 10  # The rate of the number of transactions to be created per second
        # The average transaction propagation delay in seconds (Only if Full technique is used)
        Tdelay = 5.1
        Tfee = 0.000062  # The average transaction fee
        Tsize = 0.000546  # The average transaction size  in MB

        ''' Node Parameters '''
        Nn = 3  # the total number of nodes in the network (NOT used)
        NODES = []
        from Models.Node import Node
        # here as an example we define three nodes by assigning a unique id for each one
        NODES = [Node(id=0), Node(id=1)]

        ''' Simulation Parameters '''
        simTime = 1000  # the simulation length (in seconds)
        Runs = 2  # Number of simulation runs

    ''' Input configurations for Bitcoin model '''
    if model == 1:
        ''' Block Parameters '''
        Binterval = 600  # Average time (in seconds)for creating a block in the blockchain
        Bsize = 1.0  # The block size in MB
        Bdelay = 0.42  # average block propogation delay in seconds, #Ref: https://bitslog.wordpress.com/2016/04/28/uncle-mining-an-ethereum-consensus-protocol-flaw/
        Breward = 12.5  # Reward for mining a block

        ''' Transaction Parameters '''
        hasTrans = True  # True/False to enable/disable transactions in the simulator
        Ttechnique = "Light"  # Full/Light to specify the way of modelling transactions
        Tn = 10  # The rate of the number of transactions to be created per second
        # The average transaction propagation delay in seconds (Only if Full technique is used)
        Tdelay = 5.1
        Tfee = 0.000062  # The average transaction fee
        Tsize = 0.000546  # The average transaction size  in MB

        ''' Node Parameters '''
        Nn = 3  # the total number of nodes in the network
        NODES = []
        from Models.Bitcoin.Node import Node
        # here as an example we define three nodes by assigning a unique id for each one + % of hash (computing) power
        NODES = [Node(id=0, hashPower=50), Node(
            id=1, hashPower=20), Node(id=2, hashPower=30)]

        ''' Simulation Parameters '''
        simTime = 10000  # the simulation length (in seconds)
        Runs = 2  # Number of simulation runs

    ''' Input configurations for Ethereum model '''
    if model == 2:

        ''' Block Parameters '''
        Binterval = 6.21  # Average time (in seconds)for creating a block in the blockchain
        Bsize = 1.0  # The block size in MB
        Blimit = 8000000  # The block gas limit
        Bdelay = 6  # average block propogation delay in seconds, #Ref: https://bitslog.wordpress.com/2016/04/28/uncle-mining-an-ethereum-consensus-protocol-flaw/
        Breward = 2  # Reward for mining a block

        ''' Transaction Parameters '''
        hasTrans = True  # True/False to enable/disable transactions in the simulator
        Ttechnique = "Light"  # Full/Light to specify the way of modelling transactions
        Tn = 20  # The rate of the number of transactions to be created per second
        # The average transaction propagation delay in seconds (Only if Full technique is used)
        Tdelay = 3
        # The transaction fee in Ethereum is calculated as: UsedGas X GasPrice
        Tsize = 0.000546  # The average transaction size  in MB

        ''' Drawing the values for gas related attributes (UsedGas and GasPrice, CPUTime) from fitted distributions '''

        ''' Uncles Parameters '''
        hasUncles = True  # boolean variable to indicate use of uncle mechansim or not
        Buncles = 2  # maximum number of uncle blocks allowed per block
        Ugenerations = 7  # the depth in which an uncle can be included in a block
        Ureward = 0
        UIreward = Breward / 32  # Reward for including an uncle

        ''' Node Parameters '''
        Nn = 100  # the total number of nodes in the network (NOT used)

        from Models.Ethereum.Node import Node
        # here as an example we define three nodes by assigning a unique id for each one + % of hash (computing) power
        NODES = []
        auto_gen_nodes = False

        if auto_gen_nodes == True:
            for i in range(100): # Number of nodes: change to range(X) to populate network with X nodes
                NODES.append(Node(id=i, hashPower=1))
        else:
            NODES.append(Node(id=0, hashPower=20))
            NODES.append(Node(id=1, hashPower=10))
            NODES.append(Node(id=2, hashPower=15))
            NODES.append(Node(id=3, hashPower=5))
            NODES.append(Node(id=4, hashPower=5))
            NODES.append(Node(id=5, hashPower=10))
            NODES.append(Node(id=6, hashPower=15))
            NODES.append(Node(id=7, hashPower=10))
            NODES.append(Node(id=8, hashPower=5))
            NODES.append(Node(id=9, hashPower=5))

        ''' Simulation Parameters '''
        simTime = 500  # the simulation length (in seconds)
        Runs = 4  # Number of simulation runs
