def natural_index_of (coll, x):
  ''' Returns the index of x in coll, plus 1.
      This is useful for ZooKeeper or Kafka style host IDs.
  '''
  return coll.index(x) + 1

def unroll_address(x):
  if type(x) is list or type(x) is tuple:
    return x[0]['private_ip_address']
  else:
    return x['private_ip_address']

def private_addresses(coll):
  return map(unroll_address, coll)

class FilterModule(object):
    ''' Ansible Jinja2 filters '''

    def filters(self):
      return {
        'natural_index_of': natural_index_of,
        'private_addresses': private_addresses,
      }
