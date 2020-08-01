from xldtools import XldRepo

a = XldRepo('Infrastructure/testapp3')
print (a.create_repository(host_type="overthere.SshHost", host_os="UNIX", host_address="2.2.2.3"))
