import oci
import json

from oci.util import to_dict
#from oci.config import from_file

config = oci.config.from_file("/root/.oci/config", "DEFAULT")

#config = from_file()  # Config file is read from user's home location i.e., ~/.oci/config

COMPARTMENT_ID="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq" # root compartment OCID

identity_client = oci.identity.IdentityClient(config)

list_compartments_response = identity_client.list_compartments(
    compartment_id=COMPARTMENT_ID,
    compartment_id_in_subtree=True)

# Get the list of compartments including child compartments except root compartment
compartmentlist = list_compartments_response.data

# Get the details of root compartment & append to the compartment list so that we have the full list of compartments in the given tenancy

root_compartment = identity_client.get_compartment(compartment_id=COMPARTMENT_ID).data

compartmentlist.append(root_compartment)

#print(compartmentlist[0].name)

for x in compartmentlist:
    print(x.name,"-----",x.description)

#datos_diccionario = json.loads(compartmentlist)
#datos_diccionario = json.dumps(compartmentlist)
#print(datos_diccionario["name"])

tcl = type(compartmentlist)
print("tipo de objeto de compartmentlist:",tcl)
