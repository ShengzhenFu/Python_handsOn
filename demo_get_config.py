import mod_config

otdf_log=mod_config.getConfig("app_settings", "otdf_loader_log_file")
output_otdf_list=mod_config.getConfig("app_settings","output_otdf_list")
keyword1=mod_config.getConfig("app_settings", "keyword1")
keyword2=mod_config.getConfig("app_settings", "keyword2")
mail_to=mod_config.getConfig("app_settings", "mail_to")
mail_from=mod_config.getConfig("app_settings", "mail_from")
smtp_server=mod_config.getConfig("app_settings", "smtp_server")
smtp_port=mod_config.getConfig("app_settings", "smtp_port")
smtp_username=mod_config.getConfig("app_settings", "smtp_username")
smtp_password=mod_config.getConfig("app_settings", "smtp_password")
mail_title=mod_config.getConfig("app_settings", "mail_title")
mail_content=mod_config.getConfig("app_settings", "mail_content")

print(mail_title)
logfle=otdf_log
f=open(logfle, 'r')
s=f.readlines()
print(s)
f.close()

