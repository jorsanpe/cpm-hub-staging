CPM_HUB_BITS_DIRECTORY = cpm-hub/bits
CPM_HUB_AUTH_USERS_DIRECTORY = cpm-hub-auth/users
BIT_DEVELOPERS_DIRECTORY = agents/bit_developers
BIT_USERS_DIRECTORY = agents/bit_users

all: simulation

simulation: cpm-hub/cpm-hub/build/cpm-hub
	mkdir -p $(CPM_HUB_BITS_DIRECTORY)
	mkdir -p $(CPM_HUB_AUTH_USERS_DIRECTORY)
	mkdir -p $(BIT_DEVELOPERS_DIRECTORY)
	mkdir -p $(BIT_USERS_DIRECTORY)
	docker-compose build
	docker-compose up

cpm-hub/cpm-hub/build/cpm-hub:
	cd cpm-hub/cpm-hub && cpm install && cpm build

clean:
	$(RM) -r $(CPM_HUB_BITS_DIRECTORY)
	$(RM) -r $(CPM_HUB_AUTH_USERS_DIRECTORY)
	$(RM) -r $(BIT_DEVELOPERS_DIRECTORY)
	$(RM) -r $(BIT_USERS_DIRECTORY)

.PHONY: simulation clean cpm-hub/cpm-hub/build/cpm-hub
