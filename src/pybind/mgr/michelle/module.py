
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
#	try:
#		process = subprocess.Popen(['mail', '-s', 'mail from ceph', mail_to],
#				       stdin=subprocess.PIPE)
#	except Exception, error:
#		print error
#	process.communicate(mail_body)
    	fromaddr='ceph@ceph.gabotyafot.com'
    	subject="Testing..."
    	cmd= 'echo '+mail_body+' | mail -s '+subject+' -r '+fromaddr+' '+mail_to
    	send=subprocess.call(cmd,shell=True)

    def handle_command(self, inbuf, cmd):
	self.send_message(cmd['mail_to'],cmd['mail_body'])
        status_code = 0
        output_buffer = "Output buffer is for data results"
        output_string = "Output string is for informative text"

	
        return status_code, output_buffer,  output_string
