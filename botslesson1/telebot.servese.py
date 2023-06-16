[Unit]
Description=Telegram Bot
After=network.target

[Service]
User=vladimir
Group=vladimir

WorkingDirectory=/home/vladimir/tele_bot/
Environment="PYTHONPATH=/home/vladimir/tele_bot/"
ExecStart=/home/lupizdrik/telebot/.venv/bin/python /home/lupizdrik/telebot/ubuntu18/bot.py

[Install]
WantedBy=multi-user.target