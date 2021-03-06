#!/bin/bash
echo "Removing Solana ..."

# Stop solana
systemctl stop solana

# Disable solana on startup
systemctl disable solana

# Remove service file from systemd
rm /etc/systemd/system/solana.service

# Reload daemon
systemctl daemon-reload

# Remove solana folders
rm -r /root/solana
rm -r /root/solana_update
rm -r /root/solanamonitoring
rm -r /root/.local/share/solana

# Remove Zabbix
rm /root/nodemon.sh
rm /root/slotBehind.py
rm /root/zabbix-release*
rm -r /etc/zabbix
rm -r /var/log/zabbix
systemctl stop zabbix-agent 
systemctl disable zabbix-agent
apt-get --purge remove -y zabbix-*
