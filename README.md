<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
![Twitter Follow](https://img.shields.io/twitter/follow/nurettinyakit?style=social)



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)

<!-- ABOUT THE PROJECT -->
## About The Project

This is a python project to read large & search large CSV files using `dask` which provides `pandas dataframe`

The sample dataset includes more than `1000000` (1 million) lines. And it's larger than `100MB`.

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com) -->

### Built With

* Python

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have

* [dask](https://dask.org/)

```
pip install dask.dataframe
```


<!-- USAGE EXAMPLES -->
## Usage

- CSV file is in the `/data` folder.
- Put your CSV to the `/data` folder.
- Provide the path of the CSV in the `load_csv_to_dataframe` method.
- Change `search_column` to your column name.
- Create the list that you wanna search for by replacing the items in `create_search_items_list` method.
- Run the application.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/NurettinYAKIT/CSV/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nurettinyakit/CSV.svg?style=flat
[contributors-url]: https://github.com/nurettinyakit/CSV/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nurettinyakit/CSV.svg?style=flat
[forks-url]: https://github.com/nurettinyakit/CSV/network/members
[stars-shield]: https://img.shields.io/github/stars/nurettinyakit/CSV.svg?style=flat
[stars-url]: https://github.com/nurettinyakit/CSV/stargazers
[issues-shield]: https://img.shields.io/github/issues/nurettinyakit/CSV.svg?style=flat
[issues-url]: https://github.com/nurettinyakit/CSV/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/nurettinyakit

<!--[product-screenshot]: images/screenshot.png -->