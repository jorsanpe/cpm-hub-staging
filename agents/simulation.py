import bit_developer_agent
import bit_user_agent
import agent_names


# name = agent_names.new_agent_name()
# bit_user = bit_user_agent.BitUserAgent(name)

name = agent_names.new_agent_name()
bit_developer = bit_developer_agent.BitDeveloperAgent(name)
# bit_developer.request_invitation_token()

for i in range(40):
    bit_developer.next_step()
