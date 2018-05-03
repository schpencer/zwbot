
# Zero-Width Steganography

This project was submitted as my final project for Digital Forensics 2 at the University of Illinois Urbana - Champaign (UIUC). The intention of this project is to highlight a possible use case for information hiding with zero-width characters. 

Zero width characters have previously been used to fingerprint text due to their invisibility in most user facing scenarios. In this project, I present a template for embedding botnet instructions inside a message, which can then be posted to Twitter. By doing so, a Command Server could hypothetically run in plain sight.


## Getting Started

### Prerequisites

The only dependency used is the python-twitter module. The module can be installed with pip

```
pip install python-twitter
```

### Installing

#### Command Encoder
Clone or download the repository.
Edit tweet.<span></span>py to include your Twitter API keys
Edit main.<span></span>py to include the commands you wish to execute. Example commands are provided inside main.<span></span>py.


The program is run with Python 3
```
python command_encoder/main.py
```
  
#### Zero Width Scout

To install the Chrome Extension, navigate to chrome://extensions/

The packed extension can be installed directly by dragging and dropping the zero_width_scout.crx file onto this page. 

You can also enable Developer Mode and load the unpacked extension manually by selecting the chrome_extension folder in the repo.

## Implemented Botnet Commands

A small subset of Agobot commands were implemented from multiple categories in order to demonstrate the steganography method. These commands were obtained from a list maintained by the [Honeynet Project](https://www.honeynet.org/node/55)


### DDoS something

**ddos.stop**  
```
stops all floods
```
**ddos.phatwonk [host] [time] [delay]**  
```
Starts a SYN-flood on ports 21,22,23,25,53,80,81,88,  
110,113,119,135,137,139,143,443,445,1024,1025,1433,  
1500,1720,3306,3389,5000,6667,8000,8080
```

### Downloading files from the internet
**http.update**  
```
executes a file from a given HTTP URL
```

## Dead ends
Unfortunately, not all of my ideas worked and made their way into this repo. I had initially wanted to explore how Zero Width characters would be displayed inside Wireshark. I had tried to hide information in the User-Agent or other HTTP header fields. Unfortunately Wireshark displays non-ascii characters as '.', so the existence of the Zero-Width characters was obvious. This path was quickly scrapped and the focus was switched towards the user facing side, such as a Twitter account.

## Authors

*  **Spencer Schrock** 

## License

This project is licensed under the MIT License.

## Acknowledgments

* T.J Crowder whose work was used and cited inside the chrome extension

* Zach Aysan for his article on fingerprinting text with zero-width characters, which inspired this project

* The Honeynet Project for their list of Botnet Commands
