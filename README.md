# Wazuh-n8n-Workflow

This repository contains an example integration between Wazuh and n8n.  
It enables sending Wazuh alerts via a webhook to n8n and processing them automatically.

The included files allow you to forward alerts from Wazuh to n8n and enrich them with AI-based analysis and recommendations.

---

## Repository Contents

### `custom-n8n`
- A **Bash script** executed by Wazuh when an alert is triggered.
- Sends alert data to the configured n8n webhook.
- **Installation:**
  ```bash
  sudo cp custom-n8n /var/ossec/integrations/
  sudo chown root:wazuh /var/ossec/integrations/custom-n8n
  sudo chmod +x /var/ossec/integrations/custom-n8n
  ```

---

### `custom-n8n.py`
- A **Python script** also used for the integration with n8n.
- Contains logic to pre-process alert data before sending it to n8n.
- **Installation:**
  ```bash
  sudo cp custom-n8n.py /var/ossec/integrations/
  sudo chown root:wazuh /var/ossec/integrations/custom-n8n.py
  sudo chmod +x /var/ossec/integrations/custom-n8n.py
  ```

---

### `AI-Agent-Prompt.txt`
- A **prompt** for an AI that generates an HTML output from the received Wazuh alert.
- The HTML output includes:
  - The essential information of the alert
  - Recommended actions to respond to the alert

---

### `ossec.conf.txt`
- Contains the **configuration snippet** that must be added to `/var/ossec/etc/ossec.conf`.
- Enables the webhook integration by triggering `custom-n8n` when alerts are created.
- **Important:** Without this configuration, the webhook will not be triggered.

---

## Usage

1. **Install integration scripts**
   ```bash
   sudo cp custom-n8n /var/ossec/integrations/
   sudo cp custom-n8n.py /var/ossec/integrations/

   sudo chown root:wazuh /var/ossec/integrations/custom-n8n
   sudo chown root:wazuh /var/ossec/integrations/custom-n8n.py

   sudo chmod +x /var/ossec/integrations/custom-n8n
   sudo chmod +x /var/ossec/integrations/custom-n8n.py
   ```

2. **Configure Wazuh**
   - Open `/var/ossec/etc/ossec.conf`
   - Insert the contents of `ossec.conf.txt`
   - Restart the Wazuh manager

3. **Configure n8n webhook**
   - Create a webhook workflow in n8n to receive the alert data
   - Use the prompt from `AI-Agent-Prompt.txt` to let an AI process and summarize the alert data

---

## License

This project is free to use.  

