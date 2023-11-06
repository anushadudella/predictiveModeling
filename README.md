<br />
<a name="readme-top"></a>
<div align="center">

<h2 align="center">Quantifying the Impact of the COVID-19 Pandemic on Mental Health
Searches Using Time Series Modeling, Euclidean Distance and
Granger’s Causality</h2>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

COVID-19 is a contagious disease caused by the virus severe acute respiratory syndrome (SARS-CoV-2). Since its
introduction in Wuhan, China in 2019, this virus has spread to over 213 countries worldwide and was most
prevalent in the United States. While related diseases and variants of COVID-19 are tracked via the CDC
surveillance systems, increases of mental health disorders are under-estimated. According to the Kaiser Family
Foundation, concerns about mental health and substance abuse remain elevated three years after the onset of the
COVID-19 pandemic. As the topic of mental health is closely related to social media and a user’s search trends, I
decided to establish this relationship and predict google search frequencies of mental health related keywords based
on numbers of COVID-19 cases. The objective of my research is to quantify the impact of the COVID-19 pandemic
on the the potential increase of these mental health related keywords.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][python.com]][python-url]
* [![scikitlearn][scikitlearn.com]][scikitlearn-url]
* [![numpy][numpy.com]][numpy-url]
* [![plotly][plotly.com]][plotly-url]
* [![matplotlib][matplotlib.com]][matplotlib-url]




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Project Files and Usage

| **Python File Names**  | **Description**                                                         | **Output**                       | **Input**           | Hypothesis | **** |
|------------------------|-------------------------------------------------------------------------|----------------------------------|----------------------|------------|------|
| linearreg.py           | Creates the linear regression model                                     | linear_reg_op.txt                | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | III        |      |    
| grangercasuality.py    | Creates the granger casuality test                                      | granger_op.txt                   | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | III        |      |  
| arimamodel.py          | Creates the arima model                                                 | ADHDPrediction_ARIMA.jpeg        | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | III        |      |  
| calcCorrCoeff.py       | Calculates the correlation coefficent                                   | corr_coeff_op.txt                | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | III        |      |
| stateWithEuclidDist.py | Calculates Euclidean Distance for a State with 2 different Time Periods | state_euclid_dist_op.txt         | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | II         |      |   
| getting_two_states.py  | Comparing two states for COVID searches                                 | getTwoStates.jpeg                | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | II         |      |   
| twoRegionEuclidDist.py | Calculates Euclidean distance between two regions                       | twoRegionEuclidDist.jpeg         | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | II         |      |      
| oneRegion.py           | Creates a graph for freq of keyword for one region                      | anxiety_over_twotimeperiods.jpeg | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | I          |      |      
| oneRegionEuclidDist.py | Calculates Euclidean distance for one region (two time periods)         | onregion_op.txt                  | us_counties_2020.csv, us_counties_2021.csv, us_counties_2022.csv | I          |      |      

                   

### Prerequisites

Please follow the below instructions to install the required software to run this project.

* python
  ```sh
  sudo apt install python
  ```
* numpy / scikit-learn / pandas / matplotlib / plotly 
  ```sh
  pip install pandas
  pip install numpy
  pip install matplotlib
  pip install plotly
  pip install scikit-learn
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/anushadudella/predictiveModeling.git
   ```
2. Download the data files us-counties-2020.csv, us-counties-2021.csv, us-counties-2022.csv from the [![New York Times][newyorktimes.com]][newyorktimes-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the following command to create the graphs and corresponding output files.

**Hypothesis I - Correlation between Google Searches of keywords and COVID-19**
   ```sh
   python oneRegion.py
   python oneRegionEuclidDist.py
   ```

**Hypothesis II - State A more than State B**
   ```sh
   python twoRegionEuclidDist.py
   python stateWithEuclidDist.py
   python getting_two_states.py
   ```

**Hypothesis III - COVID-19 Case Trends**
   ```sh
   python calcCorrCoeff.py
   python grangerCasuality.py
   python linearreg.py
   python arimamodel.py
 
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

** Steps to generate Presentation **

   ```sh
   cd ./Presentation
   ./pdflatex AnushaDudella_PredictiveModelingPresentation.tex  
 
   ```

** Steps to generate Research Paper **
AnushaDudella_PredictiveModelingResearchPaper_nodate.tex
   ```sh
   cd ./Paper
   ./pdflatex AnushaDudella_PredictiveModelingResearchPaper_nodate.tex  
 
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

** Steps to generate Side Project Presentation **
Anusha_Dudella_MoleculeVisualizing.tex
   ```sh
   cd ./SideProject
   ./pdflatex Anusha_Dudella_MoleculeVisualizing.tex 
 
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the [[GPL 3.0 License ]](https://www.gnu.org/licenses/gpl-3.0.en.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Anusha Dudella  - anusharao4262@gmail.com<br>
[Anusha Dudella LinkedIn][linkedin-url]


Project Link: [https://github.com/anushadudella/predictiveModeling](https://github.com/anushadudella/predictiveModeling)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Del Valle, Sara Y][sarah-url]
* [Hulley, Selina Amanda]
* [Mark Emry][emry-url]
* [Mark Galassi][galassi-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[plotly.com]: https://img.shields.io/badge/plotly-563D7C?style=for-the-badge&logo=plotly&logoColor=white
[plotly-url]: https://plotly.com
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/AnushaDudella
[numpy.com]: https://img.shields.io/badge/numpy-0769AD?style=for-the-badge&logo=numpy&logoColor=white
[numpy-url]: https://numpy.org
[python.com]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org
[scikitlearn.com]: https://img.shields.io/badge/scikitlearn-0769AD?style=for-the-badge&logo=scikitlearn&logoColor=white
[scikitlearn-url]: https://scikitlearn.org
[matplotlib.com]: https://img.shields.io/badge/matplotlib-0769AD?style=for-the-badge&logo=matplotlib&logoColor=white
[matplotlib-url]: https://matplotlib.org
[newyorktimes.com]: https://img.shields.io/badge/newyorktimes-0769AD?style=for-the-badge&logo=newyorktimes&logoColor=white
[newyorktimes-url]: https://newyorktimes.com
[galassi-url]: https://galassi.org
[sarah-url]: https://public.lanl.gov/sdelvall/
[emry-url]: https://mcneil.roundrockisd.org/team/mark-emry/


