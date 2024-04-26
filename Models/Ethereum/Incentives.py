from InputsConfig import InputsConfig as p
from Models.Consensus import Consensus as c
from Models.Incentives import Incentives as BaseIncentives
from Statistics import Statistics


class Incentives(BaseIncentives):
    """
	 Defines the rewarded elements (block + transactions), calculate and distribute the rewards among the participating nodes
    """

    def uncle_rewards(bc):
         for uncle in bc.uncles:
                for k in p.NODES:
                       if uncle.miner == k.id:
                             Statistics.totalUncles +=1
                             uncle_height = uncle.depth # uncle depth
                             block_height = bc.depth# block depth
                             k.uncles+=1
                             # DEBUG (disable uncle rewards)
                             # k.balance += ((uncle_height - block_height + 8) * p.Breward / 8) # Reward for mining an uncle block

    ''' rewards for the miner who included in the incle block in his block '''
    def uncle_inclusion_rewards(bc):
         Ru=0 # uncle reward is set to 0
         for uncle in bc.uncles:
            Ru += p.UIreward
         return Ru

    def distribute_rewards():
        total = 0
        total_reward = 0

        # DEBUG
        congestion_factor = 100
        node_to_reward_dict = {}
        node_list_copy = p.NODES.copy()
        node_list_copy.sort(key=lambda x: x.balance, reverse=False)

        # DEBUG
        for bc in c.global_chain:
            for node in p.NODES:
                if bc.miner == node.id:
                    total += 1
                    total_reward += p.Breward

        # DEBUG
        print(f"Distributing {total_reward} total rewards among {total} miners (Ethereum model)...\n")

        # We distribute rewards in descending order: node with least balance gets most
        for block in c.global_chain:
            for node in node_list_copy:
                if block.miner == node.id:
                    if total_reward >= 0:
                        cur_reward = total_reward / congestion_factor

                        node_to_reward_dict[node.id] = cur_reward
                        total_reward -= cur_reward # reward becomes what's left overe after distribution to current node

        for block in c.global_chain:
            for node in p.NODES:
                if block.miner == node.id:
                    node.blocks += 1
                    #node.balance += p.Breward # increase the miner balance by the block reward
                    if node.id in node_to_reward_dict:
                        node.balance += node_to_reward_dict[node.id]
                    tx_fee = Incentives.transactions_fee(block)
                    node.balance += tx_fee # add transaction fees to balance
                    node.balance += Incentives.uncle_inclusion_rewards(block) # add uncle inclusion rewards to balance
            Incentives.uncle_rewards(block) # add uncle generation rewards for the miner who build the uncle block

        # DEBUG
        if True:
            for node in p.NODES:
                print(f"Node with node.id == {node.id} has balance {node.balance}")
