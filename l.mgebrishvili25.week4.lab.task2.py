@@ -0,0 +1,61 @@
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4029b064-8e4e-47e6-9a91-47f121ba3bd9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save tls_report.txt using UTF-8 encoding for Jupyter compatibility\n",
    "\n",
    "report = \"\"\"Task 2: SSL/TLS in HTTPS – Summary Report\n",
    "\n",
    "1. TLS Handshake Explanation:\n",
    "When I visited https://www.nasa.gov, my browser and the NASA server used the TLS handshake to set up a secure connection. The handshake started with a \"Client Hello\" message from my browser, and the server responded with a \"Server Hello\" and a digital certificate. This certificate proved the server’s identity and included the encryption methods it supports. After agreeing on a shared encryption key, all communication between my browser and the server became encrypted and protected.\n",
    "\n",
    "2. What protects against Man-in-the-Middle (MITM) attacks in TLS:\n",
    "TLS prevents MITM attacks through encryption and authentication. The digital certificate used in the handshake is signed by a trusted Certificate Authority, and my browser verifies it. Only the real server has the correct private key to complete the handshake. If an attacker tries to pretend to be the server, the handshake will fail. Encryption ensures that no one in the middle can read or change the data during the session.\n",
    "\n",
    "3. How TLS is used in websites (TLS in HTTPS):\n",
    "HTTPS means \"HTTP over TLS.\" Every time I visit a secure website like https://www.nasa.gov, TLS protects the connection by encrypting the data being sent and received. It makes sure that passwords, credit card numbers, and other sensitive information can’t be seen or changed by others. TLS also ensures that I’m really talking to the correct website and not a fake version created by attackers.\n",
    "\n",
    "Screenshots of the TLS certificate, supported cipher suites, and the Wireshark TLS handshake have been included in this submission as proof of testing and analysis.\n",
    "\"\"\"\n",
    "\n",
    "# Write to file with UTF-8 encoding\n",
    "with open(\"tls_report.txt\", \"w\", encoding=\"utf-8\") as file:\n",
    "    file.write(report)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72f4572a-57ac-4b68-b4f4-3672489353ec",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}