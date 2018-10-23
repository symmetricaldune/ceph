
"""
A module to send an email via mail command from shell

"""

from mgr_module import MgrModule


class Module(MgrModule):
    COMMANDS = [
        {
            "cmd": "mail name=mail_to,type=CephString " \
                   "name=mail_body,type=CephString",
            "desc": "Sends an email via shell",
            "perm": "r"
        },
    ]

    def send_message(self, mail_to,  mail_body):
	import subprocess
    	fromaddr='ceph@ceph.gabotyafot.com' ## todo - fix from address with internal ceph data
    	subject="Hello from ceph"
	#mail_body_with_addons = mail_body + str(self.get('health')) ## todo - check how to parse and make health output beautiful
    	cmd= 'echo '+mail_body+' | mail -s '+subject+' -r '+fromaddr+' '+mail_to
    	send=subprocess.call(cmd,shell=True)

    def handle_command(self, inbuf, cmd):
	self.send_message(cmd['mail_to'],cmd['mail_body'])
        status_code = 0
        output_buffer = "Output buffer is for data results"
        output_string = "Output string is for informative text"

	
        return status_code, output_buffer,  output_string
