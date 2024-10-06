# Installing Grafana and Configuring Prometheus

## Step 1: Install Grafana

1. **Download and Add Grafana GPG Key**:
   ```bash
   wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
   ```

2. **Add Grafana APT Repository**:
   ```bash
   echo "deb https://packages.grafana.com/oss/release/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
   ```

3. **Update Package List**:
   ```bash
   sudo apt-get update
   ```

4. **Install Grafana**:
   ```bash
   sudo apt-get install grafana
   ```

5. **Locate the Grafana Server Binary**:
   ```bash
   find /usr -name grafana-server
   ```

6. **Change to the Bin Directory**:
   ```bash
   cd /usr/share/grafana/bin
   ```

7. **Start Grafana Server**:
   ```bash
   sudo ./grafana-server web
   ```

## Step 2: Access Grafana

1. Open your web browser and go to:
   ```
   http://localhost:3000
   ```

2. **Log In to Grafana**:
   - **Username**: `admin`
   - **Password**: `admin` (you’ll be prompted to change this on the first login).

## Step 3: Configure Prometheus as a Data Source

1. **Open Configuration Menu**:
   In the Grafana sidebar, click on the gear icon (⚙️) to open the **Configuration** menu.

2. **Add Data Source**:
   - Click on **Data Sources**.
   - Click on **Add data source**.

3. **Select Prometheus**:
   Choose **Prometheus** from the list.

4. **Enter HTTP URL**:
   In the **HTTP URL** field, enter:
   ```
   http://localhost:9090
   ```

5. **Save and Test**:
   Click **Save & Test** to verify the connection. You should see a message confirming that the data source is working.

## Step 4: Create a New Dashboard

1. **Create New Dashboard**:
   In the sidebar, click on the **+** icon and select **Dashboard**.

2. **Add New Panel**:
   - Click on **Add new panel**.

## Step 5: Query Prometheus Metrics

1. **Enter Prometheus Query**:
   In the new panel, you’ll see a query editor. Enter your Prometheus query to visualize your metrics. For example, to visualize the total number of HTTP requests, use:
   ```promql
   http_requests_total
   ```
