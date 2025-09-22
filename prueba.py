from aplicacionweb1.utils import leeMysql
import mysql.connector


texto= "In the Linux kernel, the following vulnerability has been resolved:\n\ndrm/amd/display: Add more checks for DSC / HUBP ONO guarantees\n\n[WHY]\nFor non-zero DSC instances it's possible that the HUBP domain required\nto drive it for sequential ONO ASICs isn't met, potentially causing\nthe logic to the tile to enter an undefined state leading to a system\nhang.\n\n[HOW]\nAdd more checks to ensure that the HUBP domain matching the DSC instance\nis appropriately powered.\n\n(cherry picked from commit da63df07112e5a9857a8d2aaa04255c4206754ec)"

texto1= "In the Linux kernel, the following vulnerability has been resolved:\n\ndrm/amd/display: Add more checks for DSC / HUBP ONO guarantees\n\n[WHY]\nFor non-zero DSC instances it's possible that the HUBP domain required\nto drive it for sequential ONO ASICs isn't met, potentially causing\nthe logic to the tile to enter an undefined state leading to a system\nhang.\n\n[HOW]\nAdd more checks to ensure that the HUBP domain matching the DSC instance\nis appropriately powered.\n\n(cherry picked from commit da63df07112e5a9857a8d2aaa04255c4206754ec)"

texto3="ocid1.vsshostvulnerability.oc1..aaaaaaaa6iwiba6larpvobb2qqk6grzvw7ea4ojktkphz7okvzii6fgbdwzq"

print(len(texto3))

#print(leeMysql())

#for x in leeMysql():
#    print(leeMysql[x])
