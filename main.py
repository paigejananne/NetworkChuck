#string
camping_stuff = "tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, flash drive, beard oil, marshmallows"

#list
#ordered
#zero-indexed
camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

#who brings what?
me = camping_list[4]

you = camping_list[3]

#negative index
#access last item in list
them = camping_list[-1]

print(me)

print(you)

print(them)

print(camping_list)

#methods
supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 95.5, False]

#add to list (one at a time) to end of list
supplies.append("toilet paper")

supplies.append("bidet")

#add to list(multiple pieces of data) to end of list
supplies.extend(["formula", "diapers"])

supplies = supplies + ["dog food", "treats"]

#add to list to beginning
supplies.insert(0,"blankets")

#add to list second to last
supplies.insert(-1, "leashes")

print(supplies)
