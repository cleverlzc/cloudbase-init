# Copyright 2013 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


NAME0 = "eth0"
MAC0 = "fa:16:3e:2d:ec:cd"
ADDRESS0 = "10.0.0.15"
NETMASK0 = "255.255.255.0"
BROADCAST0 = "10.0.0.255"
GATEWAY0 = "10.0.0.1"
DNSNS0 = "208.67.220.220 208.67.222.222"

NAME1 = "eth1"
ADDRESS1 = "10.1.0.2"
NETMASK1 = "255.255.255.0"
BROADCAST1 = "10.1.0.255"
GATEWAY1 = "10.1.0.1"


def get_fake_metadata_json(version):
    data1 = {
        "random_seed": "Wn51FGjZa3vlZtTxJuPr96oCf+X8jqbA9U2XR5wNdnApy1fz"
                       "/2NNssUwPoNzG6etw9RBn+XiZ0zKWnFzMsTopaN7WwYjWTnI"
                       "sVw3cpIkTd579wQgoEr1ANqhfO3qTvkOVNMhzTAw1ps+wqRm"
                       "kLxH+1qYJnX06GcdKRRGkWTaOSlTkieA0LO2oTGFlbFDWcOW"
                       "2vT5BvSBmqP7vNLzbLDMTc7MIWRBzwmtcVPC17QL6EhZJTUc"
                       "Z0mTz7l0R0DocLmFwHEXFEEr+q4WaJjt1ejOOxVM3tiT7D8Y"
                       "pRZnnGNPfvEhq1yVMUoi8yv9pFmMmXicNBhm6zDKVjcWk0gf"
                       "bvaQcMnnOLrrE1VxAAzyNyPIXBI/H7AAHz2ECz7dgd2/4ocv"
                       "3bmTRY3hhcUKtNuat2IOvSGgMBUGdWnLorQGFz8t0/bcYhE0"
                       "Dve35U6Hmtj78ydV/wmQWG0iq49NX6hk+VUmZtSZztlkbsaa"
                       "7ajNjZ+Md9oZtlhXZ5vJuhRXnHiCm7dRNO8Xo6HffEBH5A4s"
                       "mQ1T2Kda+1c18DZrY7+iQJRifa6witPCw0tXkQ6nlCLqL2we"
                       "JD1XMiTZLSM/XsZFGGSkKCKvKLEqQrI/XFUq/TA6B4aLGFlm"
                       "mhOO/vMJcht06O8qVU/xtd5Mv/MRFzYaSG568Z/mhk4vYLYd"
                       "QYAA+pXRW9A=",
        "uuid": "4b32ddf7-7941-4c36-a854-a1f5ac45b318",
        "availability_zone": "nova",
        "hostname": "windows.novalocal",
        "launch_index": 0,
        "public_keys": {
            "key":
                "ssh-rsa "
                "AAAAB3NzaC1yc2EAAAADAQABAAABA"
                "QDf7kQHq7zvBod3yIZs0tB/AOOZz5pab7qt/h"
                "78VF7yi6qTsFdUnQxRue43R/75wa9EEyokgYR"
                "LKIN+Jq2A5tXNMcK+rNOCzLJFtioAwEl+S6VL"
                "G9jfkbUv++7zoSMOsanNmEDvG0B79MpyECFCl"
                "th2DsdE4MQypify35U5ri5Qi7E6PEYAsU65LF"
                "MG2boeCIB29BEooE6AgPr2DuJeJ+2uw+YScF9"
                "FV3og4Wyz5zipPVh8YpVev6dlg0tRWUrCtZF9"
                "IODpCTrT3vsPRG3xz7CppR+vGi/1gLXHtJCRj"
                "frHwkY6cXyhypNmkU99K/wMqSv30vsDwdnsQ1"
                "q3YhLarMHB Generated by Nova\n",
            0: "windows"
        },
        "network_config": {
            "content_path": "network",
            "debian_config": ("""
# Injected by Nova on instance boot
#
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto {name0}
iface {name0} inet static
    hwaddress ether {mac0}
    address {address0}
    netmask {netmask0}
    broadcast {broadcast0}
    gateway {gateway0}
    dns-nameservers {dnsns0}

auto {name1}
iface {name1} inet static
    address {address1}
    netmask {netmask1}
    broadcast {broadcast1}
    gateway {gateway1}
         """).format(name0=NAME0,    # eth0 (IPv4)
                     mac0=MAC0,
                     address0=ADDRESS0,
                     broadcast0=BROADCAST0,
                     netmask0=NETMASK0,
                     gateway0=GATEWAY0,
                     dnsns0=DNSNS0,
                     # eth1 (IPv4)
                     name1=NAME1,
                     address1=ADDRESS1,
                     broadcast1=BROADCAST1,
                     netmask1=NETMASK1,
                     gateway1=GATEWAY1)
        }
    }

    datadict = {
        "2013-04-04": data1
    }

    return datadict.get(version)
