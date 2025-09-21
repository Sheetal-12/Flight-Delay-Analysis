# ✈️ Flight Delay Analysis Dashboard

A comprehensive Streamlit dashboard for analyzing flight delays in the US, featuring interactive visualizations, key performance indicators, and dynamic filtering capabilities.

## 🌟 Features

- **Real-time KPIs**: Total flights, delayed flights, and average departure/arrival delays
- **Interactive Visualizations**:
  - Average delay by airline
  - Average delay by day of week
  - Flight duration vs departure delay scatter plot
  - Percentage of delayed flights over time
  - Heatmap of average delay by airline vs day of week
- **Dynamic Filters**: Filter by airline, month, and day of week for customized insights
- **Containerized Deployment**: Docker support for easy deployment

## 📁 Project Structure

```
Flight-Delay-Analysis/
│
├── app.py                    # Main Streamlit application
├── data/                     # Dataset directory
│   ├── raw/                  # Full dataset (not committed to repo)
│   └── sample/              # Sample dataset for testing
├── src/                     # Source code modules
│   ├── data_loader.py       # Data loading utilities
│   ├── visuals.py          # Visualization functions
│   └── kpis.py             # KPI calculation functions
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container configuration
└── README.md               # Project documentation
```

## 📊 Dataset Information

The dashboard uses flight data from Kaggle: [2023 US Civil Flights - Delay, Meteo, and Aircraft](https://www.kaggle.com/datasets/bordanova/2023-us-civil-flights-delay-meteo-and-aircraft?select=US_flights_2023.csv)

### Dataset Options:
- **Sample Dataset**: `flight_data_sample.csv` included in `data/sample/` for quick testing
- **Full Dataset**: Place the complete dataset in `data/raw/US_flights_2023.csv` and set `sample=False` in `load_data()` function

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd Flight-Delay-Analysis
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   
   # On Linux/macOS
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**:
   ```bash
   streamlit run app.py
   ```

The dashboard will be available at `http://localhost:8501`

## 🧪 Testing

Run the test suite to ensure all components are working correctly:

```bash
pytest tests/
```

## 🐳 Docker Deployment

### Build and run with Docker:

```bash
# Build the image
docker build -t flight-delay-dashboard .

# Run the container
docker run -p 8501:8501 flight-delay-dashboard
```

Access the dashboard at `http://localhost:8501`

## 📈 Dashboard Components

### Key Performance Indicators (KPIs)
- **Total Flights**: Complete count of flights in the dataset
- **Delayed Flights**: Number and percentage of delayed flights
- **Average Delays**: Mean departure and arrival delay times

### Visualizations
- **Airline Performance**: Compare average delays across different airlines
- **Temporal Analysis**: Understand delay patterns by day of week and over time
- **Correlation Analysis**: Explore relationships between flight duration and delays
- **Heat Map**: Comprehensive view of delays by airline and day combinations

### Interactive Filters
- **Airline Selection**: Focus on specific carriers
- **Month Filter**: Analyze seasonal patterns
- **Day of Week**: Examine weekday vs weekend performance

## 🛠️ Development

### Project Structure Explained
- `app.py`: Main Streamlit application entry point
- `src/data_loader.py`: Handles data loading and preprocessing
- `src/visuals.py`: Contains all visualization functions
- `src/kpis.py`: Calculates key performance indicators
- `tests/`: Unit tests for reliability and maintainability

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure functionality
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Support

If you encounter any issues or have questions, please open an issue in the repository.

---

**Happy analyzing! ✈️📊**