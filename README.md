# Bike Sharing Data Analysis Dashboard

This project provides an interactive **Streamlit** dashboard for analyzing and visualizing bike sharing data. The dashboard allows users to explore rental trends based on hourly usage, monthly usage, and seasonal patterns.

### Features:
- **Overview**: Displays summary statistics for both hourly and daily bike sharing data.
- **Hourly Rentals**: Allows users to view the average bike rentals per hour for **Registered Users**, **Casual Users**, or **All Users** during weekdays and weekends.
- **Monthly Rentals**: Provides insights into bike usage trends on a monthly basis.
- **Seasonal Rentals**: Displays bike usage patterns across different seasons (Spring, Summer, Fall, Winter).

## Requirements

To run this dashboard locally, you will need Python 3.x and the necessary libraries. These dependencies are listed in the `requirements.txt` file.

### Installation Instructions:

1. **Clone the repository** or **Download the project files** to your local machine.

   If you're cloning via Git, run:
   ```bash
   git clone https://github.com/triababtista/bikesharing.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd bikesharing
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit Dashboard**:
   To launch the dashboard, run the following command:
   ```bash
   streamlit run app.py
   ```

6. **Access the Dashboard**:
   After running the command, open your browser and go to the following URL:
   ```bash
   http://localhost:8501
   ```

   You should see the interactive dashboard where you can select user types, view hourly and seasonal bike rental trends, and more.

## Project Structure

- `dashboard.py`: The main Streamlit application script.
- `hour.csv`: The dataset containing hourly bike rental data.
- `day.csv`: The dataset containing daily bike rental data.
- `requirements.txt`: The file listing the required Python libraries and their versions.
- `README.md`: This documentation file.

## How It Works

The Streamlit app allows users to explore the bike-sharing dataset with the following features:

1. **Overview**: Displays descriptive statistics for both hourly and daily datasets.
2. **Hourly Rentals**: Users can choose a user type (Casual Users, Registered Users, or All Users) and view how bike rentals vary by hour for weekdays vs weekends.
3. **Monthly Rentals**: Users can explore the average bike usage by month.
4. **Seasonal Rentals**: Users can examine the average bike usage by season (Spring, Summer, Fall, Winter).

### Selecting User Types:
In the **Hourly Rentals** section, you can choose between:
- **Casual Users**: Rentals by users who rent bikes casually.
- **Registered Users**: Rentals by users who are registered in the bike-sharing system.
- **All Users**: Aggregated data for both registered and casual users.
