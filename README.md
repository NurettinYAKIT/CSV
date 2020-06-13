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


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project

This is a python project to read large & search large CSV files using `dask` which provides `pandas dataframe`

The sample dataset includes more than `1000000` (1 million) lines. And it's larger than `100MB`.

[![Product Name Screen Shot][product-screenshot]](https://example.com)

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

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Nurettin Onur YAKIT - [@NurettinYAKIT](https://twitter.com/NurettinYAKIT) - onuryakit@gmail.com

Project Link: [https://github.com/NurettinYAKIT/CSV](https://github.com/NurettinYAKIT/CSV)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nurettinyakit/CSV.svg?style=flat-square
[contributors-url]: https://github.com/nurettinyakit/CSV/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nurettinyakit/CSV.svg?style=flat-square
[forks-url]: https://github.com/nurettinyakit/CSV/network/members
[stars-shield]: https://img.shields.io/github/stars/nurettinyakit/CSV.svg?style=flat-square
[stars-url]: https://github.com/nurettinyakit/CSV/stargazers
[issues-shield]: https://img.shields.io/github/issues/nurettinyakit/CSV.svg?style=flat-square
[issues-url]: https://github.com/nurettinyakit/CSV/issues
[license-shield]: https://img.shields.io/github/license/nurettinyakit/CSV.svg?style=flat-square
[license-url]: https://github.com/nurettinyakit/CSV/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/nurettinyakit
[product-screenshot]: images/screenshot.png