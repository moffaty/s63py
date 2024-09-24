import s63py
import os

hw_id = bytearray.fromhex("3131313131")
m_key = bytearray.fromhex("3031323334")
m_id = bytearray.fromhex("3031")

s63client = s63py.S63Client(hw_id, m_key, m_id)

user_permit = s63client.getUserpermit()

s63_cell_path = "charts/2/ENC_ROOT/RU/RU3NSKI9/6/0/RU3NSKI9.000"
output_cell_path = "charts/s57/RU3NSKI9.000"
cellpermit = "RU3NSKI92013121915F890F859EA6C4B15F890F859EA6C4B66A84600136CC76D"

cell_keys = s63py.extractCellKeysFromCellpermit(cellpermit,hw_id)
s63py.decryptAndUnzipCellByKey(s63_cell_path,cell_keys,output_cell_path)
