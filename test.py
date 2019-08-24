from odoo_api import OdooApi

host = "http://odoo12:8012"
db = "test"
username = "yasser"
password = "1"


if __name__ == '__main__':
    api=OdooApi(host,db,username,password)
    api.getVersion()
    api.getUid()
    api.checkAccessRights()
    print(api.search1('product.template',[[['list_price', '>', '100']]]))
    print(api.search2('product.template', [[['list_price', '>', '100']]],['name']))
    print(api.search3('product.template', [[['list_price', '>', '100']]],offset=10))
    print(api.search4('product.template', [[['list_price', '>', '100']]],['name'],offset=10))
    print(api.search5('product.template', [[['list_price', '>', '100']]],offset=10,limit=2))
    print(api.search6('product.template', [[['list_price', '>', '100']]],['name'],offset=10,limit=2))
    print(api.count('product.template', [[['list_price', '>', '100']]]))
    print(api.delete('product.template',[10,8]))
    print(api.create('product.template',[{'name':'yasser'}]))
    print(api.getMetaData('product.template',[],['string','ttype']))
    print(api.read('product.template',[23],['name','type']))
    print(api.update('product.template',23,{'name':'JASDF'}))



