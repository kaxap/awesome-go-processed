This is a processed copy of https://raw.githubusercontent.com/avelino/awesome-go/master/README.md. Updated 2018-05-12

# Awesome Go

[![Build Status](https://travis-ci.org/avelino/awesome-go.svg?branch=master)](https://travis-ci.org/avelino/awesome-go) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Slack Widget](https://camo.githubusercontent.com/984828c0b020357921853f59eaaa65aaee755542/68747470733a2f2f73332e65752d63656e7472616c2d312e616d617a6f6e6177732e636f6d2f6e6774756e612f6a6f696e2d75732d6f6e2d736c61636b2e706e67)](http://gophers.slack.com/messages/awesome)

A curated list of awesome Go frameworks, libraries and software. Inspired by [awesome-python](https://github.com/vinta/awesome-python).

### Contributing

Please take a quick gander at the [contribution guidelines](https://github.com/avelino/awesome-go/blob/master/CONTRIBUTING.md) first. Thanks to all [contributors](https://github.com/avelino/awesome-go/graphs/contributors); you rock!

#### *If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you!*

### Contents

- [Awesome Go](#awesome-go)
    - [Audio and Music](#audio-and-music)
    - [Authentication and OAuth](#authentication-and-oauth)
    - [Command Line](#command-line)
    - [Configuration](#configuration)
    - [Continuous Integration](#continuous-integration)
    - [CSS Preprocessors](#css-preprocessors)
    - [Data Structures](#data-structures)
    - [Database](#database)
    - [Database Drivers](#database-drivers)
    - [Date and Time](#date-and-time)
    - [Distributed Systems](#distributed-systems)
    - [Email](#email)
    - [Embeddable Scripting Languages](#embeddable-scripting-languages)
    - [Files](#files)
    - [Financial](#financial)
    - [Forms](#forms)
    - [Game Development](#game-development)
    - [Generation and Generics](#generation-and-generics)
    - [Geographic](#geographic)
    - [Go Compilers](#go-compilers)
    - [Goroutines](#goroutines)
    - [GUI](#gui)
    - [Hardware](#hardware)
    - [Images](#images)
    - [IoT](#iot-internet-of-things)
    - [Logging](#logging)
    - [Machine Learning](#machine-learning)
    - [Messaging](#messaging)
    - [Miscellaneous](#miscellaneous)
    - [Natural Language Processing](#natural-language-processing)
    - [Networking](#networking)
    - [OpenGL](#opengl)
    - [ORM](#orm)
    - [Package Management](#package-management)
    - [Query Language](#query-language)
    - [Resource Embedding](#resource-embedding)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Security](#security)
    - [Serialization](#serialization)
    - [Template Engines](#template-engines)
    - [Testing](#testing)
    - [Text Processing](#text-processing)
    - [Third-party APIs](#third-party-apis)
    - [Utilities](#utilities)
    - [Validation](#validation)
    - [Version Control](#version-control)
    - [Video](#video)
    - [Web Frameworks](#web-frameworks)
        - [Middlewares](#middlewares)
            - [Actual middlewares](#actual-middlewares)
            - [Libraries for creating HTTP middlewares](#libraries-for-creating-http-middlewares)
        - [Routers](#routers)
    - [Windows](#windows)
    - [XML](#xml)

- [Tools](#tools)
    - [Code Analysis](#code-analysis)
    - [Editor Plugins](#editor-plugins)
	- [Go Generate Tools](#go-generate-tools)
    - [Go Tools](#go-tools)
    - [Software Packages](#software-packages)
        - [DevOps Tools](#devops-tools)
        - [Other Software](#other-software)

- [Server Applications](#server-applications)

- [Resources](#resources)
    - [Benchmarks](#benchmarks)
    - [Conferences](#conferences)
    - [E-Books](#e-books)
    - [Gophers](#gophers)
    - [Meetups](#meetups)
    - [Twitter](#twitter)
    - [Websites](#websites)
        - [Tutorials](#tutorials)

## Audio and Music

*Libraries for manipulating audio.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|207|14|2|* [waveform](https://github.com/mdlayher/waveform) - Go package capable of generating waveform images from audio streams.|
|196|15|6|* [music-theory](https://github.com/go-music-theory/music-theory) - Music theory models in Go.|
|192|38|4|* [PortAudio](https://github.com/gordonklaus/portaudio) - Go bindings for the PortAudio audio I/O library.|
|163|41|11|* [portmidi](https://github.com/rakyll/portmidi) - Go bindings for PortMidi.|
|78|13|11|* [mix](https://github.com/go-mix/mix) - Sequence-based Go-native audio mixer for music apps.|
|74|8|2|* [flac](https://github.com/eaburns/flac) - Native Go FLAC decoder.|
|68|15|6|* [go-sox](https://github.com/krig/go-sox) - libsox bindings for go.|
|67|9|0|* [mp3](https://github.com/tcolgate/mp3) - Native Go MP3 decoder.|
|61|12|4|* [id3v2](https://github.com/bogem/id3v2) - Fast and stable ID3 parsing and writing library for Go.|
|60|14|3|* [flac](https://github.com/mewkiz/flac) - Native Go FLAC decoder.|
|56|16|3|* [taglib](https://github.com/wtolson/go-taglib) - Go bindings for taglib.|
|41|3|4|* [gaad](https://github.com/Comcast/gaad) - Native Go AAC bitstream parser.|
|23|4|0|* [malgo](https://github.com/gen2brain/malgo) - Mini audio library.|
|19|5|3|* [vorbis](https://github.com/mccoyst/vorbis) - "Native" Go Vorbis decoder (uses CGO, but has no dependencies).|
|16|6|1|* [go_mediainfo](https://github.com/zhulik/go_mediainfo) - libmediainfo bindings for go.|
|9|1|0|* [EasyMIDI](https://github.com/algoGuy/EasyMIDI) - EasyMidi is a simple and reliable library for working with standard midi file (SMF).|
|8|0|1|* [minimp3](https://github.com/tosone/minimp3) - Lightweight MP3 decoder library.|
|3|0|0|* [gosamplerate](https://github.com/dh1tw/gosamplerate) - libsamplerate bindings for go.|
## Authentication and OAuth

*Libraries for implementing authentications schemes.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3526|355|37|* [jwt-go](https://github.com/dgrijalva/jwt-go) - Golang implementation of JSON Web Tokens (JWT).|
|2368|229|17|* [casbin](https://github.com/hsluoyz/casbin) - Authorization library that supports access control models like ACL, RBAC, ABAC.|
|1674|199|31|* [goth](https://github.com/markbates/goth) - provides a simple, clean, and idiomatic way to use OAuth and OAuth2. Handles multiple providers out of the box.|
|1588|399|57|* [oauth2](https://github.com/golang/oauth2) - Successor of goauth2. Generic OAuth 2.0 package that comes with JWT, Google APIs, Compute Engine and App Engine support.|
|1402|285|45|* [osin](https://github.com/RangelReale/osin) - Golang OAuth2 server library.|
|1379|94|21|* [authboss](https://github.com/volatiletech/authboss) - Modular authentication system for the web. It tries to remove as much boilerplate and "hard things" as possible so that each time you start a new web project in Go, you can plug it in, configure, and start building your app without having to build an authentication system each time.|
|857|112|15|* [go-jose](https://github.com/square/go-jose) - Fairly complete implementation of the JOSE working group's JSON Web Token, JSON Web Signatures, and JSON Web Encryption specs.|
|847|110|8|* [go-oauth2-server](https://github.com/RichardKnop/go-oauth2-server) - Standalone, specification-compliant,  OAuth2 server written in Golang.|
|829|44|4|* [gologin](https://github.com/dghubble/gologin) - chainable handlers for login with OAuth1 and OAuth2 authentication providers.|
|714|109|2|* [gorbac](https://github.com/mikespook/gorbac) - provides a lightweight role-based access control (RBAC) implementation in Golang.|
|583|45|13|* [loginsrv](https://github.com/tarent/loginsrv) - JWT login microservice with plugable backends such as OAuth2 (Github), htpasswd, osiam.|
|262|20|0|* [permissions2](https://github.com/xyproto/permissions2) - Library for keeping track of users, login states and permissions. Uses secure cookies and bcrypt.|
|197|52|17|* [Go-AWS-Auth](https://github.com/smartystreets/go-aws-auth) - AWS (Amazon Web Services) request signing library.|
|140|16|2|* [httpauth](https://github.com/goji/httpauth) - HTTP Authentication middleware.|
|111|6|2|* [paseto](https://github.com/o1egl/paseto) - Golang implementation of Platform-Agnostic Security Tokens (PASETO)|
|111|11|0|* [jwt-auth](https://github.com/adam-hanna/jwt-auth) - JWT middleware for Golang http servers with many configuration options.|
|86|11|3|* [yubigo](https://github.com/GeertJohan/yubigo) - Yubikey client package that provides a simple API to integrate the Yubico Yubikey into a go application.|
|61|6|5|* [session](https://github.com/icza/session) - Go session management for web servers (including support for Google App Engine - GAE).|
|40|9|7|* [jwt](https://github.com/robbert229/jwt) - Clean and easy to use implementation of JSON Web Tokens (JWT).|
|29|0|1|* [sessions](https://github.com/adam-hanna/sessions) - Dead simple, highly performant, highly customizable sessions service for go http servers.|
|19|2|2|* [securecookie](https://github.com/chmike/securecookie) - Efficient secure cookie encoding/decoding.|
|4|0|0|* [sessiongate-go](https://github.com/f0rmiga/sessiongate-go) - Go session management using the SessionGate Redis module.|
|3|0|0|* [signedvalue](https://github.com/sashka/signedvalue) - Signed and timestamped strings compatible with [Tornado's](https://github.com/tornadoweb/tornado) `create_signed_value`, `decode_signed_value`, and therefore `set_secure_cookie` and `get_secure_cookie`.|
|1|0|0|* [jwt](https://github.com/pascaldekloe/jwt) - Lightweight JSON Web Token (JWT) library.|
|0|0|0|* [cookiestxt](https://github.com/mengzhuo/cookiestxt) - provides parser of cookies.txt file format.|
## Command Line

### Standard CLI

*Libraries for building standard or basic Command Line applications.*

* [climax](http://github.com/tucnak/climax) - Alternative CLI with "human face", in spirit of Go command.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|8088|707|107|* [urfave/cli](https://github.com/urfave/cli) - Simple, fast, and fun package for building command line apps in Go (formerly codegangsta/cli).|
|7494|606|119|* [cobra](https://github.com/spf13/cobra) - Commander for modern Go CLI interactions.|
|4076|317|215|* [drive](https://github.com/odeke-em/drive) - Google Drive client for the commandline.|
|1849|139|16|* [kingpin](https://github.com/alecthomas/kingpin) - Command line and flag parser supporting sub commands.|
|1126|101|40|* [readline](https://github.com/chzyer/readline) - Pure golang implementation that provides most features in GNU-Readline under MIT license.|
|1014|133|16|* [go-flags](https://github.com/jessevdk/go-flags) - go command line option parser.|
|936|71|15|* [docopt.go](https://github.com/docopt/docopt.go) - Command-line arguments parser that will make you smile.|
|819|71|21|* [cli-init](https://github.com/tcnksm/gcli) - The easy way to start building Golang command line applications.|
|806|63|10|* [mitchellh/cli](https://github.com/mitchellh/cli) - Go library for implementing command-line interfaces.|
|514|40|7|* [mow.cli](https://github.com/jawher/mow.cli) - Go library for building CLI applications with sophisticated flag and argument parsing and validation.|
|473|24|2|* [go-arg](https://github.com/alexflint/go-arg) - Struct-based argument parsing in Go.|
|448|24|0|* [complete](https://github.com/posener/complete) - Write bash completions in Go + Go command bash completion.|
|444|63|2|* [liner](https://github.com/peterh/liner) - Go readline-like library for command-line interfaces.|
|382|113|19|* [pflag](https://github.com/spf13/pflag) - Drop-in replacement for Go's flag package, implementing POSIX/GNU-style --flags.|
|367|31|16|* [cli](https://github.com/mkideal/cli) - Feature-rich and easy to use command-line package based on golang struct tags.|
|85|10|5|* [ukautz/clif](https://github.com/ukautz/clif) - Small command line interface framework.|
|76|2|4|* [flag](https://github.com/cosiner/flag) - Simple but powerful command line option parsing library for Go supporting subcommand.|
|57|1|1|* [commandeer](https://github.com/jaffee/commandeer) - Dev-friendly CLI apps: sets up flags, defaults, and usage based on struct fields and tags.|
|52|5|3|* [sflags](https://github.com/octago/sflags) - Struct based flags generator for flag, urfave/cli, pflag, cobra, kingpin and other libraries.|
|47|7|1|* [wmenu](https://github.com/dixonwille/wmenu) - Easy to use menu structure for cli applications that prompts users to make choices.|
|29|4|5|* [argparse](https://github.com/akamensky/argparse) - Command line argument parser inspired by Python's argparse module.|
|28|1|1|* [cli](https://github.com/teris-io/cli) - Simple and complete API for building command line interfaces in Go.|
|24|2|0|* [wlog](https://github.com/dixonwille/wlog) - Simple logging interface that supports cross-platform color and concurrency.|
|20|0|0|* [strumt](https://github.com/antham/strumt) - Library to create prompt chain.|
|18|1|0|* [env](https://github.com/codingconcepts/env) - Tag-based environment configuration for structs.|
|14|0|2|* [gocmd](https://github.com/devfacet/gocmd) - Go library for building command line applications.|
|8|1|1|* [argv](https://github.com/cosiner/argv) - Go library to split command line string as arguments array using the bash syntax.|
### Advanced Console UIs

*Libraries for building Console Applications and Console User Interfaces.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|7373|430|84|* [termui](https://github.com/gizak/termui) - Go terminal dashboard based on **termbox-go** and inspired by [blessed-contrib](https://github.com/yaronn/blessed-contrib).|
|2800|234|45|* [termbox-go](https://github.com/nsf/termbox-go) - Termbox is a library for creating cross-platform text-based interfaces.|
|2439|160|29|* [gocui](https://github.com/jroimartin/gocui) - Minimalist Go library aimed at creating Console User Interfaces.|
|2340|193|9|* [color](https://github.com/fatih/color) - Versatile package for colored terminal output.|
|1510|47|15|* [go-prompt](https://github.com/c-bata/go-prompt) - Library for building a powerful interactive prompt, inspired by [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit).|
|1327|72|15|* [tui-go](https://github.com/marcusolsson/tui-go) - Go UI library for building rich terminal applications.|
|1114|66|17|* [uiprogress](https://github.com/gosuri/uiprogress) - Flexible library to render progress bars in terminal applications.|
|647|29|12|* [uilive](https://github.com/gosuri/uilive) - Library for updating terminal output in realtime.|
|429|16|2|* [uitable](https://github.com/gosuri/uitable) - Library to improve readability in terminal apps using tabular data.|
|293|10|1|* [aurora](https://github.com/logrusorgru/aurora) - ANSI terminal colors that supports fmt.Printf/Sprintf.|
|274|10|2|* [progressbar](https://github.com/schollz/progressbar) - Basic thread-safe progress bar that works in every OS.|
|271|41|3|* [go-colorable](https://github.com/mattn/go-colorable) - Colorable writer for windows.|
|251|12|2|* [chalk](https://github.com/ttacon/chalk) - Intuitive package for prettifying terminal/console output.|
|241|29|0|* [go-isatty](https://github.com/mattn/go-isatty) - isatty for golang.|
|217|22|2|* [mpb](https://github.com/vbauerster/mpb) - Multi progress bar for terminal applications.|
|170|13|2|* [go-colortext](https://github.com/daviddengcn/go-colortext) - Go library for color output in terminals.|
|143|14|7|* [termtables](https://github.com/apcera/termtables) - Go port of the Ruby library [terminal-tables](https://github.com/tj/terminal-table) for simple ASCII table generation as well as providing markdown and HTML output.|
|39|3|0|* [cfmt](https://github.com/mingrammer/cfmt) - Contextual fmt inspired by bootstrap color classes.|
|12|2|0|* [colourize](https://github.com/TreyBastian/colourize) - Go library for ANSI colour text in terminals.|
|5|1|0|* [go-ataman](https://github.com/workanator/go-ataman) - Go library for rendering ANSI colored text templates in terminals.|
|4|0|0|* [tabular](https://github.com/InVisionApp/tabular) - Print ASCII tables from command line utilities without the need to pass large sets of data to the API.|
|0|0|0|* [gommon/color](https://github.com/labstack/gommon/tree/master/color) - Style terminal text.|
## Configuration

*Libraries for configuration parsing.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|5205|504|225|* [viper](https://github.com/spf13/viper) - Go configuration with fangs.|
|1195|75|10|* [godotenv](https://github.com/joho/godotenv) - Go port of Ruby's dotenv library (Loads environment variables from `.env`).|
|928|146|5|* [ini](https://github.com/go-ini/ini) - Go package to read and write INI files.|
|472|46|3|* [env](https://github.com/caarlos0/env) - Parse environment variables to Go structs (with defaults).|
|223|11|2|* [store](https://github.com/tucnak/store) - Lightweight configuration manager for Go.|
|192|8|0|* [joshbetz/config](https://github.com/joshbetz/config) - Small configuration library for Go that parses environment variables, JSON files, and reloads automatically on SIGHUP.|
|151|30|3|* [config](https://github.com/olebedev/config) - JSON or YAML configuration wrapper with environment variables and flags parsing.|
|123|12|1|* [hjson](https://github.com/hjson/hjson-go) - Human JSON, a configuration file format for humans. Relaxed syntax, fewer mistakes, more comments.|
|115|10|0|* [envconfig](https://github.com/vrischmann/envconfig) - Read your configuration from environment variables.|
|87|7|0|* [envcfg](https://github.com/tomazk/envcfg) - Un-marshaling environment variables to Go structs.|
|85|0|0|* [envh](https://github.com/antham/envh) - Helpers to manage environment variables.|
|80|19|2|* [gcfg](https://github.com/go-gcfg/gcfg) - read INI-style configuration files into Go structs; supports user-defined types and subsections.|
|69|10|4|* [goConfig](https://github.com/crgimenes/goConfig) - Parses a struct as input and populates the fields of this struct with parameters from command line, environment variables and configuration file.|
|52|7|0|* [gofigure](https://github.com/ian-kent/gofigure) - Go application configuration made easy.|
|40|2|6|* [confita](https://github.com/heetch/confita) - Load configuration in cascade from multiple backends into a struct.|
|36|6|2|* [configure](https://github.com/paked/configure) - Provides configuration through multiple sources, including JSON, flags and environment variables.|
|16|1|0|* [ingo](https://github.com/schachmat/ingo) - Flags persisted in an ini-like config file.|
|16|4|1|* [mini](https://github.com/sasbury/mini) - Golang package for parsing ini-style configuration files.|
|11|0|0|* [go-up](https://github.com/ufoscout/go-up) - A simple configuration library with recursive placeholders resolution and no magic.|
|6|2|0|* [envconf](https://github.com/ian-kent/envconf) - Configuration from environment.|
|3|0|1|* [xdg](https://github.com/OpenPeeDeeP/xdg) - Cross platform package that follows the [XDG Standard](https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html).|
|0|0|0|* [gone/jconf](https://github.com/One-com/gone/tree/master/jconf) - Modular JSON configuration. Keep you config structs along with the code they configure and delegate parsing to submodules without sacrificing full config serialization.|
## Continuous Integration

*Tools for help with continuous integration.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|14238|1506|102|* [drone](https://github.com/drone/drone) - Drone is a Continuous Integration platform built on Docker, written in Go.|
|479|73|14|* [goveralls](https://github.com/mattn/goveralls) - Go integration for Coveralls.io continuous code coverage tracking system.|
|89|20|1|* [overalls](https://github.com/go-playground/overalls) - Multi-Package go project coverprofile for tools like goveralls.|
|7|0|0|* [roveralls](https://github.com/LawrenceWoodman/roveralls) - Recursive coverage testing tool.|
|1|0|0|* [gomason](https://github.com/nikogura/gomason) - Test, Build, Sign, and Publish your go binaries from a clean workspace.|
## CSS Preprocessors

*Libraries for preprocessing CSS files.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|403|26|47|* [c6](https://github.com/c9s/c6) - High performance SASS compatible-implementation compiler written in Go.|
|402|24|8|* [gcss](https://github.com/yosssi/gcss) - Pure Go CSS Preprocessor.|
|81|13|9|* [go-libsass](https://github.com/wellington/go-libsass) - Go wrapper to the 100% Sass compatible libsass project.|
## Data Structures

*Generic datastructures and algorithms in Go.*

|stars|forks|issues|description|
| --- | --- | --- | --- |
|4078|395|14|* [gods](https://github.com/emirpasic/gods) - Go Data Structures. Containers, Sets, Lists, Stacks, Maps, BidiMaps, Trees, HashSet etc.|
|4065|434|14|* [go-datastructures](https://github.com/Workiva/go-datastructures) - Collection of useful, performant, and thread-safe data structures.|
|933|56|5|* [boomfilters](https://github.com/tylertreat/BoomFilters) - Probabilistic data structures for processing continuous, unbounded streams.|
|734|83|4|* [golang-set](https://github.com/deckarep/golang-set) - Thread-Safe and Non-Thread-Safe high-performance sets for Go.|
|583|28|0|* [hyperloglog](https://github.com/axiomhq/hyperloglog) - HyperLogLog implementation with Sparse, LogLog-Beta bias correction and TailCut space reduction.|
|519|56|27|* [gota](https://github.com/kniren/gota) - Implementation of dataframes, series, and data wrangling methods for Go.|
|440|79|4|* [willf/bloom](https://github.com/willf/bloom) - Go package implementing Bloom filters.|
|404|39|39|* [roaring](https://github.com/RoaringBitmap/roaring) - Go package implementing compressed bitsets.|
|366|68|4|* [bitset](https://github.com/willf/bitset) - Go package implementing bitsets.|
|306|19|4|* [cuckoofilter](https://github.com/seiflotfy/cuckoofilter) - Cuckoo filter: a good alternative to a counting bloom filter implemented in Go.|
|276|32|3|* [go-geoindex](https://github.com/hailocab/go-geoindex) - In-memory geo index.|
|265|17|5|* [mafsa](https://github.com/smartystreets/mafsa) - MA-FSA implementation with Minimal Perfect Hashing.|
|261|36|8|* [trie](https://github.com/derekparker/trie) - Trie implementation in Go.|
|153|32|2|* [goskiplist](https://github.com/ryszard/goskiplist) - Skip list implementation in Go.|
|129|21|2|* [hilbert](https://github.com/google/hilbert) - Go package for mapping values to and from space-filling curves, such as Hilbert and Peano curves.|
|112|9|1|* [bloom](https://github.com/zhenjl/bloom) - Bloom filters implemented in Go.|
|84|10|0|* [binpacker](https://github.com/zhuangsirui/binpacker) - Binary packer and unpacker helps user build custom binary stream.|
|82|8|1|* [encoding](https://github.com/zhenjl/encoding) - Integer Compression Libraries for Go.|
|77|1|0|* [go-rquad](https://github.com/aurelien-rainone/go-rquad) - Region quadtrees with efficient point location and neighbour finding.|
|54|5|1|* [ttlcache](https://github.com/diegobernardes/ttlcache) - In-memory LRU string-interface{} map with expiration for golang.|
|52|6|1|* [merkletree](https://github.com/cbergoon/merkletree) - Implementation of a merkle tree providing an efficient and secure verification of the contents of data structures.|
|50|9|1|* [skiplist](https://github.com/gansidui/skiplist) - Skiplist implementation in Go.|
|37|3|0|* [count-min-log](https://github.com/seiflotfy/count-min-log) - Go implementation Count-Min-Log sketch: Approximately counting with approximate counters (Like Count-Min sketch but using less memory).|
|33|5|0|* [go-adaptive-radix-tree](https://github.com/plar/go-adaptive-radix-tree) - Go implementation of Adaptive Radix Tree.|
|32|4|0|* [conjungo](https://github.com/InVisionApp/conjungo) - A small, powerful and flexible merge library.|
|20|4|0|* [bit](https://github.com/yourbasic/bit) - Golang set data structure with bonus bit-twiddling functions.|
|17|1|0|* [levenshtein](https://github.com/agnivade/levenshtein) - Implementation to calculate levenshtein distance in Go.|
|12|0|0|* [levenshtein](https://github.com/agext/levenshtein) - Levenshtein distance and similarity metrics with customizable edit costs and Winkler-like bonus for common prefix.|
|7|1|0|* [go-mcache](https://github.com/OrlovEvgeny/go-mcache) - Fast in-memory key:value store/cache library. Pointer caches.|
|6|1|0|* [goset](https://github.com/zoumo/goset) - A useful Set collection implementation for Go.|
|6|2|0|* [algorithms](https://github.com/shady831213/algorithms) - Algorithms and data structures.CLRS study.|
|5|3|0|* [bloom](https://github.com/yourbasic/bloom) - Golang Bloom filter implementation.|
|5|0|0|* [go-ef](https://github.com/amallia/go-ef) - A Go implementation of the Elias-Fano encoding.|
|5|0|0|* [concurrent-writer](https://github.com/free/concurrent-writer) - Highly concurrent drop-in replacement for `bufio.Writer`.|
## Database

*Databases implemented in Go.*


*Database schema migration.*


*Database tools.*


*SQL query builder, libraries for building and using SQL.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|16299|2064|253|* [prometheus](https://github.com/prometheus/prometheus) - Monitoring system and time series database.|
|13391|1380|1708|* [cockroach](https://github.com/cockroachdb/cockroach) - Scalable, Geo-Replicated, Transactional Datastore.|
|13336|1922|700|* [influxdb](https://github.com/influxdb/influxdb) - Scalable datastore for metrics, events, and real-time analytics.|
|13246|1790|403|* [tidb](https://github.com/pingcap/tidb) - TiDB is a distributed SQL database. Inspired by the design of Google F1.|
|8487|730|84|* [bolt](https://github.com/boltdb/bolt) - Low-level key/value database for Go.|
|6429|756|10|* [groupcache](https://github.com/golang/groupcache) - Groupcache is a caching and cache-filling library, intended as a replacement for memcached in many cases.|
|5967|772|196|* [vitess](https://github.com/youtube/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.|
|5543|357|152|* [dgraph](https://github.com/dgraph-io/dgraph) - Scalable, Distributed, Low Latency, High Throughput Graph Database.|
|5023|361|39|* [pgweb](https://github.com/sosedoff/pgweb) - Web-based PostgreSQL database browser.|
|4626|371|168|* [jaeger](https://github.com/jaegertracing/jaeger) - A distributed tracing system.|
|3762|197|45|* [rqlite](https://github.com/rqlite/rqlite) - The lightweight, distributed, relational database built on SQLite.|
|3710|198|13|* [badger](https://github.com/dgraph-io/badger) - Fast key-value store in Go.|
|3453|707|65|* [kingshard](https://github.com/flike/kingshard) - kingshard is a high performance proxy for MySQL powered by Golang.|
|2535|296|93|* [ledisdb](https://github.com/siddontang/ledisdb) - Ledisdb is a high performance NoSQL like Redis based on LevelDB.|
|2207|281|28|* [goleveldb](https://github.com/syndtr/goleveldb) - Implementation of the [LevelDB](https://github.com/google/leveldb) key/value database in Go.|
|2066|196|19|* [tiedot](https://github.com/HouzuoGuo/tiedot) - Your NoSQL database powered by Golang.|
|1856|118|0|* [buntdb](https://github.com/tidwall/buntdb) - Fast, embeddable, in-memory key/value database for Go with custom indexing and spatial support.|
|1679|80|55|* [pREST](https://github.com/nuveo/prest) - Serve a RESTful API from any PostgreSQL database.|
|1612|270|35|* [go-cache](https://github.com/pmylund/go-cache) - In-memory key:value store/cache (similar to Memcached) library for Go, suitable for single-machine applications.|
|1583|137|59|* [xo](https://github.com/knq/xo) - Generate idiomatic Go code for databases based on existing schema definitions or custom queries supporting PostgreSQL, MySQL, SQLite, Oracle, and Microsoft SQL Server.|
|1503|129|41|* [Squirrel](https://github.com/Masterminds/squirrel) - Go library that helps you build SQL queries.|
|1464|113|5|* [BigCache](https://github.com/allegro/bigcache) - Efficient key/value cache for gigabytes of data.|
|1323|287|102|* [go-mysql-elasticsearch](https://github.com/siddontang/go-mysql-elasticsearch) - Sync your MySQL data into Elasticsearch automatically.|
|1204|189|111|* [orchestrator](https://github.com/github/orchestrator) - MySQL replication topology manager & visualizer.|
|994|264|46|* [go-mysql](https://github.com/siddontang/go-mysql) - Go toolset to handle MySQL protocol and replication.|
|945|100|41|* [sql-migrate](https://github.com/rubenv/sql-migrate) - Database migration tool. Allows embedding migrations into the application using go-bindata.|
|588|54|5|* [diskv](https://github.com/peterbourgon/diskv) - Home-grown disk-backed key-value store.|
|521|49|28|* [dat](https://github.com/mgutz/dat) - Go Postgres Data Access Toolkit.|
|503|202|5|* [cache2go](https://github.com/muesli/cache2go) - In-memory key:value cache which supports automatic invalidation based on timeouts.|
|498|25|40|* [moss](https://github.com/couchbase/moss) - Moss is a simple LSM key-value storage engine written in 100% Go.|
|487|18|2|* [eliasdb](https://github.com/krotik/eliasdb) - Dependency-free, transactional graph database with REST API, phrase search and SQL-like query language.|
|421|52|12|* [GCache](https://github.com/bluele/gcache) - Cache library with support for expirable Cache, LFU, LRU and ARC.|
|410|41|17|* [goqu](https://github.com/doug-martin/goqu) - Idiomatic SQL builder and query library.|
|353|21|2|* [Dotsql](https://github.com/gchaincl/dotsql) - Go library that helps you keep sql files in one place and use them with ease.|
|329|70|3|* [levigo](https://github.com/jmhodges/levigo) - Levigo is a Go wrapper for LevelDB.|
|304|31|1|* [gendry](https://github.com/didi/gendry) - Non-invasive SQL builder and powerful data binder.|
|235|32|16|* [ozzo-dbx](https://github.com/go-ozzo/ozzo-dbx) - Powerful data retrieval methods as well as DB-agnostic query building capabilities.|
|159|17|9|* [piladb](https://github.com/fern4lvarez/piladb) - Lightweight RESTful database engine based on stack data structures.|
|144|12|3|* [gormigrate](https://github.com/go-gormigrate/gormigrate) - Database schema migration helper for Gorm ORM.|
|131|12|5|* [scaneo](https://github.com/variadico/scaneo) - Generate Go code to convert database rows into arbitrary structs.|
|127|23|6|* [Scribble](https://github.com/nanobox-io/golang-scribble) - Tiny flat file JSON store.|
|113|12|5|* [sqrl](https://github.com/elgris/sqrl) - SQL query builder, fork of Squirrel with improved performance.|
|110|8|0|* [chproxy](https://github.com/Vertamedia/chproxy) - HTTP proxy for ClickHouse database.|
|97|12|14|* [migrate](https://github.com/golang-migrate/migrate) - Database migrations. CLI and Golang library.|
|97|33|4|* [myreplication](https://github.com/2tvenom/myreplication) - MySql binary log replication listener. Supports statement and row based replication.|
|71|8|5|* [goose](https://github.com/steinbacher/goose) - Database migration tool. You can manage your database's evolution by creating incremental SQL or Go scripts.|
|66|1|0|* [Vasto](https://github.com/chrislusf/vasto) - A distributed high-performance key-value store. On Disk. Eventual consistent. HA. Able to grow or shrink without service interruption.|
|64|2|0|* [igor](https://github.com/galeone/igor) - Abstraction layer for PostgreSQL that supports advanced functionality and uses gorm-like syntax.|
|61|13|1|* [clickhouse-bulk](https://github.com/nikepan/clickhouse-bulk) - Collects small insterts and sends big requests to ClickHouse servers.|
|56|4|1|* [darwin](https://github.com/GuiaBolso/darwin) - Database schema evolution library for Go.|
|35|12|0|* [godbal](https://github.com/xujiajun/godbal) - Database Abstraction Layer (dbal) for go. Support SQL builder and get result easily.|
|31|1|1|* [slowpoke](https://github.com/recoilme/slowpoke) - Key-value store with persistence.|
|30|1|0|* [couchcache](https://github.com/codingsince1985/couchcache) - RESTful caching micro-service backed by Couchbase server.|
|28|3|7|* [forestdb](https://github.com/couchbase/goforestdb) - Go bindings for ForestDB.|
|22|0|0|* [clusteredBigCache](https://github.com/oaStuff/clusteredBigCache) - BigCache with clustering support and individual item expiration.|
|20|2|30|* [pravasan](https://github.com/pravasan/pravasan) - Simple Migration tool - currently for MySQL but planning to soon support Postgres, SQLite, MongoDB, etc.|
|19|1|0|* [prep](https://github.com/hexdigest/prep) - Use prepared SQL statements without changing your code.|
|16|1|3|* [gondolier](https://github.com/emvicom/gondolier) - Gondolier is a library to auto migrate database schemas using structs.|
|10|1|0|* [tempdb](https://github.com/rafaeljesus/tempdb) - Key-value store for temporary items.|
|9|4|0|* [go-fixtures](https://github.com/RichardKnop/go-fixtures) - Django style fixtures for Golang's excellent built-in database/sql library.|
|8|0|0|* [rwdb](https://github.com/andizzle/rwdb) - rwdb provides read replica capability for multiple database servers setup.|
|4|0|0|* [gorocksdb](https://github.com/kapitan-k/gorocksdb) - Gorocksdb is a wrapper for [RocksDB](https://rocksdb.org) written in Go.|
|0|0|0|* [soda](https://github.com/markbates/pop/tree/master/soda) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.|
## Database Drivers

*Libraries for connecting and operating databases.*

* Relational Databases

* NoSQL Databases
    * [gocql](http://gocql.github.io) - Go language driver for Apache Cassandra.

* Search and Analytic Databases.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|11328|990|68|    * [cayley](https://github.com/google/cayley) - Graph database with support for multiple backends.|
|5347|1082|59|    * [go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) - MySQL driver for Go.|
|4370|682|5|    * [redigo](https://github.com/gomodule/redigo) - Redigo is a Go client for the Redis database.|
|4327|344|120|    * [bleve](https://github.com/blevesearch/bleve) - Modern text indexing library for go.|
|3833|511|159|    * [pq](https://github.com/lib/pq) - Pure Go Postgres driver for database/sql.|
|3524|155|18|    * [riot](https://github.com/go-ego/riot) - Go Open Source, Distributed, Simple and efficient Search Engine|
|3364|491|26|    * [redis](https://github.com/go-redis/redis) - Redis client for Golang.|
|2535|521|16|    * [elastic](https://github.com/olivere/elastic) - Elasticsearch client for Go.|
|2444|519|91|    * [go-sqlite3](https://github.com/mattn/go-sqlite3) - SQLite3 driver for go that uses database/sql.|
|1368|157|64|    * [pgx](https://github.com/jackc/pgx) - PostgreSQL driver supporting features beyond those exposed by database/sql.|
|1316|146|12|    * [gorethink](https://github.com/dancannon/gorethink) - Go language driver for RethinkDB.|
|906|252|78|    * [elastigo](https://github.com/mattbaird/elastigo) - Elasticsearch client library.|
|738|168|61|    * [go-mssqldb](https://github.com/denisenkom/go-mssqldb) - Microsoft MSSQL driver for Go.|
|684|61|10|    * [mgo](https://github.com/globalsign/mgo) - MongoDB driver for the Go language that implements a rich and well tested selection of features under a very simple API following standard Go idioms|
|563|205|17|    * [redis](https://github.com/hoisie/redis) - Simple, powerful Redis client for Go.|
|391|32|3|    * [mongo-go-driver](https://github.com/mongodb/mongo-go-driver) - Official MongoDB driver for the Go language.|
|335|52|16|    * [neoism](https://github.com/jmcvetta/neoism) - Neo4j client for Golang.|
|290|151|66|    * [go-oci8](https://github.com/mattn/go-oci8) - Oracle driver for go that uses database/sql.|
|275|78|36|    * [go-couchbase](https://github.com/couchbase/go-couchbase) - Couchbase client in Go.|
|256|108|20|    * [aerospike-client-go](https://github.com/aerospike/aerospike-client-go) - Aerospike client in Go language.|
|244|69|2|    * [gocb](https://github.com/couchbase/gocb) - Official Couchbase Go SDK.|
|177|17|0|    * [redis](https://github.com/bsm/redeo) - Redis-protocol compatible TCP servers/services.|
|165|34|4|    * [elasticsql](https://github.com/cch123/elasticsql) - Convert sql to elasticsearch dsl in Go.|
|86|16|10|    * [goracle](https://github.com/go-goracle/goracle) - Oracle driver for Go, using the ODPI-C driver|
|78|22|11|    * [firebirdsql](https://github.com/nakagami/firebirdsql) - Firebird RDBMS SQL driver for Go.|
|71|24|9|    * [go-adodb](https://github.com/mattn/go-adodb) - Microsoft ActiveX Object DataBase driver for go that uses database/sql.|
|66|13|1|    * [Neo4j-GO](https://github.com/davemeehan/Neo4j-GO) - Neo4j REST Client in golang.|
|63|33|11|    * [gofreetds](https://github.com/minus5/gofreetds) - Microsoft MSSQL driver. Go wrapper over [FreeTDS](http://www.freetds.org).|
|59|15|4|    * [arangolite](https://github.com/solher/arangolite) - Lightweight golang driver for ArangoDB.|
|53|12|2|    * [dynago](https://github.com/underarmour/dynago) - Dynago is a principle of least surprise client for DynamoDB.|
|50|7|0|    * [skizze](https://github.com/seiflotfy/skizze) - probabilistic data-structures service and storage.|
|45|31|16|    * [go-couchdb](https://github.com/fjl/go-couchdb) - Yet another CouchDB HTTP API wrapper for Go.|
|22|8|3|    * [goes](https://github.com/OwnLocal/goes) - Library to interact with Elasticsearch.|
|21|3|8|    * [neo4j](https://github.com/cihangir/neo4j) - Neo4j Rest API Bindings for Golang.|
|21|2|4|    * [goriak](https://github.com/zegl/goriak) - Go language driver for Riak KV.|
|10|4|0|    * [avatica](https://github.com/apache/calcite-avatica-go) - Apache Avatica/Phoenix SQL driver for database/sql.|
|7|1|0|    * [xredis](https://github.com/shomali11/xredis) - Typesafe, customizable, clean & easy to use Redis client.|
|7|2|0|    * [bgc](https://github.com/viant/bgc) - Datastore Connectivity for BigQuery for go.|
|5|2|0|    * [dsc](https://github.com/viant/dsc) - Datastore connectivity for SQL, NoSQL, structured files.|
|3|1|0|    * [asc](https://github.com/viant/asc) - Datastore Connectivity for Aerospike for go.|
|0|0|0|    * [gomemcache](https://github.com/bradfitz/gomemcache/) - memcache client library for the Go programming language.|
## Date and Time

*Libraries for working with dates and times.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1686|88|3|* [now](https://github.com/jinzhu/now) - Now is a time toolkit for golang.|
|612|22|6|* [dateparse](https://github.com/araddon/dateparse) - Parse date's without knowing format in advance.|
|195|17|7|* [carbon](https://github.com/uniplaces/carbon) - Simple Time extension with a lot of util methods, ported from PHP Carbon library.|
|179|17|0|* [durafmt](https://github.com/hako/durafmt) - Time duration formatting library for Go.|
|143|4|0|* [timeutil](https://github.com/leekchan/timeutil) - Useful extensions (Timedelta, Strftime, ...) to the golang's time package.|
|49|4|2|* [timespan](https://github.com/SaidinWoT/timespan) - For interacting with intervals of time, defined as a start time and a duration.|
|33|4|0|* [go-persian-calendar](https://github.com/yaa110/go-persian-calendar) - The implementation of the Persian (Solar Hijri) Calendar in Go (golang).|
|13|4|0|* [goweek](https://github.com/grsmv/goweek) - Library for working with week entity in golang.|
|12|2|0|* [date](https://github.com/rickb777/date) - Augments Time for working with dates, date ranges, time spans, periods, and time-of-day.|
|12|3|1|* [feiertage](https://github.com/wlbr/feiertage) - Set of functions to calculate public holidays in Germany, incl. specialization on the states of Germany (Bundesländer). Things like Easter, Pentecost, Thanksgiving...|
|6|1|0|* [NullTime](https://github.com/kirillDanshin/nulltime) - Nullable `time.Time`.|
|4|1|0|* [go-sunrise](https://github.com/nathan-osman/go-sunrise) - Calculate the sunrise and sunset times for a given location.|
|4|1|1|* [tuesday](https://github.com/osteele/tuesday) - Ruby-compatible Strftime function.|
|1|0|0|* [strftime](https://github.com/awoodbeck/strftime) - C99-compatible strftime formatter.|
## Distributed Systems

*Packages that help with building Distributed Systems.*

    * [dht](https://godoc.org/github.com/anacrolix/dht) - BitTorrent Kademlia DHT implementation.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|9928|1018|43|* [go-kit](https://github.com/go-kit/kit) - Microservice toolkit with support for service discovery, load balancing, pluggable transports, request tracking, etc.|
|5528|1068|102|* [grpc-go](https://github.com/grpc/grpc-go) - The Go language implementation of gRPC. HTTP/2 based RPC.|
|4392|337|0|* [micro](https://github.com/micro/micro) - Pluggable microservice toolkit and distributed systems platform.|
|4114|452|60|* [NATS](https://github.com/nats-io/gnatsd) - Lightweight, high performance messaging system for microservices, IoT, and cloud native systems.|
|2304|399|5|* [rpcx](https://github.com/smallnest/rpcx) - Distributed pluggable RPC service framework like alibaba Dubbo.|
|2178|237|21|* [torrent](https://github.com/anacrolix/torrent) - BitTorrent client package.|
|2039|164|9|* [glow](https://github.com/chrislusf/glow) - Easy-to-Use scalable distributed big data processing, Map-Reduce, DAG execution, all in pure Go.|
|1855|236|83|* [raft](https://github.com/hashicorp/raft) - Golang implementation of the Raft consensus protocol, by HashiCorp.|
|1792|362|190|* [tendermint](https://github.com/tendermint/tendermint) - High-performance middleware for transforming a state machine written in any programming language into a Byzantine Fault Tolerant replicated state machine using the Tendermint consensus and blockchain protocols.|
|1336|125|17|* [gleam](https://github.com/chrislusf/gleam) - Fast and scalable distributed map/reduce system written in pure Go and Luajit, combining Go's high concurrency with Luajit's high performance, runs standalone or distributed.|
|1165|86|15|* [emitter-io](https://github.com/emitter-io/emitter) - High performance, distributed, secure and low latency publish-subscribe platform built with MQTT, Websockets and love.|
|755|145|12|* [hprose](https://github.com/hprose/hprose-golang) - Very newbility RPC Library, support 25+ languages now.|
|477|24|8|* [heimdall](https://github.com/gojektech/heimdall) - An enchanced http client with retry and hystrix capabilities.|
|449|54|13|* [gorpc](https://github.com/valyala/gorpc) - Simple, fast and scalable RPC library for high load.|
|439|49|10|* [KrakenD](https://github.com/devopsfaith/krakend) - Ultra performant API Gateway framework with middlewares.|
|419|30|23|* [ringpop-go](https://github.com/uber/ringpop-go) - Scalable, fault-tolerant application-layer sharding for Go applications.|
|319|51|8|    * [go-peerflix](https://github.com/Sioro-Neoku/go-peerflix) - Video streaming torrent client.|
|261|16|1|* [sleuth](https://github.com/ursiform/sleuth) - Library for master-less p2p auto-discovery and RPC between HTTP services (using [ZeroMQ](https://github.com/zeromq/libzmq)).|
|205|21|13|* [digota](https://github.com/digota/digota) - grpc ecommerce microservice.|
|184|14|1|* [go-jump](https://github.com/dgryski/go-jump) - Port of Google's "Jump" Consistent Hash function.|
|180|11|5|* [go-health](https://github.com/InVisionApp/go-health) - Library for enabling asynchronous dependency health checks in your service.|
|99|2|0|* [consistent](https://github.com/buraksezer/consistent) - Consistent hashing with bounded loads.|
|63|3|1|* [jsonrpc](https://github.com/osamingo/jsonrpc) - The jsonrpc package helps implement of JSON-RPC 2.0.|
|43|15|0|* [jsonrpc](https://github.com/ybbus/jsonrpc) - JSON-RPC 2.0 HTTP client implementation.|
|35|3|0|* [celeriac](https://github.com/svcavallar/celeriac.v1) - Library for adding support for interacting and monitoring Celery workers, tasks and events in Go.|
|35|2|0|* [flowgraph](https://github.com/vectaport/flowgraph) - MPI-style ready-send coordination layer.|
|19|12|2|* [drmaa](https://github.com/dgruber/drmaa) - Job submission library for cluster schedulers based on the DRMAA standard.|
|0|0|0|* [raft](https://github.com/coreos/etcd/tree/master/raft) - Go implementation of the Raft consensus protocol, by CoreOS.|
## Email

*Libraries and tools that implement email creation and sending.*

* [chasquid](https://blitiri.com.ar/p/chasquid) - SMTP server written in Go.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|3409|212|89|* [MailHog](https://github.com/mailhog/MailHog) - Email and SMTP testing with web and API interface.|
|1243|57|11|* [hermes](https://github.com/matcornic/hermes) - Golang package that generates clean, responsive HTML e-mails.|
|875|108|17|* [email](https://github.com/jordan-wright/email) - A robust and flexible email library for Go.|
|420|54|23|* [go-imap](https://github.com/emersion/go-imap) - IMAP library for clients and servers.|
|345|128|58|* [SendGrid](https://github.com/sendgrid/sendgrid-go) - SendGrid's Go library for sending email.|
|142|16|10|* [Hectane](https://github.com/hectane/hectane) - Lightweight SMTP client providing an HTTP API.|
|119|22|8|* [douceur](https://github.com/aymerick/douceur) - CSS inliner for your HTML emails.|
|47|14|4|* [go-message](https://github.com/emersion/go-message) - Streaming library for the Internet Message Format and mail messages.|
|40|5|0|* [smtp](https://github.com/mailhog/smtp) - SMTP server protocol state machine.|
|37|15|1|* [go-dkim](https://github.com/toorop/go-dkim) - DKIM library, to sign & verify email.|
|0|0|0|* [Gomail](https://github.com/go-gomail/gomail/) - Gomail is a very simple and powerful package to send emails.|
## Embeddable Scripting Languages

*Embedding other languages inside your go code.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3736|331|74|* [otto](https://github.com/robertkrimen/otto) - JavaScript interpreter written in Go.|
|2120|206|18|* [gopher-lua](https://github.com/yuin/gopher-lua) - Lua 5.1 VM and compiler written in Go.|
|1248|82|30|* [go-lua](https://github.com/Shopify/go-lua) - Port of the Lua 5.2 VM to pure Go.|
|663|70|19|* [go-python](https://github.com/sbinet/go-python) - naive go bindings to the CPython C-API.|
|662|53|22|* [anko](https://github.com/mattn/anko) - Scriptable interpreter written in Go.|
|569|64|5|* [go-duktape](https://github.com/olebedev/go-duktape) - Duktape JavaScript engine bindings for Go.|
|466|61|8|* [go-php](https://github.com/deuill/go-php) - PHP bindings for Go.|
|393|112|10|* [golua](https://github.com/aarzilli/golua) - Go bindings for Lua C API.|
|392|27|2|* [gisp](https://github.com/jcla1/gisp) - Simple LISP in Go.|
|294|30|20|* [agora](https://github.com/PuerkitoBio/agora) - Dynamically typed, embeddable programming language in Go.|
|22|2|2|* [purl](https://github.com/ian-kent/purl) - Perl 5.18.2 embedded in Go.|
|12|2|1|* [binder](https://github.com/alexeyco/binder) - Go to Lua binding library, based on [gopher-lua](https://github.com/yuin/gopher-lua).|
|10|0|0|* [ngaro](https://github.com/db47h/ngaro) - Embeddable Ngaro VM implementation enabling scripting in Retro.|
## Files

*Libraries for  handling files and file systems.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1434|146|42|* [afero](https://github.com/spf13/afero) - FileSystem Abstraction System for Go.|
|341|40|31|* [notify](https://github.com/rjeczalik/notify) - File system event notification library with simple API, similar to os/signal.|
|26|2|0|* [skywalker](https://github.com/dixonwille/skywalker) - Package to allow one to concurrently go through a filesystem with ease.|
|22|7|0|* [go-csv-tag](https://github.com/artonge/go-csv-tag) - Load csv file using tag.|
|18|1|0|* [tarfs](https://github.com/posener/tarfs) - Implementation of the [`FileSystem` interface](https://godoc.org/github.com/kr/fs#FileSystem) for tar files.|
|5|3|0|* [go-gtfs](https://github.com/artonge/go-gtfs) - Load gtfs files in go.|
## Financial

*Packages for accounting and finance.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|918|140|21|* [decimal](https://github.com/shopspring/decimal) - Arbitrary-precision fixed-point decimal numbers.|
|548|43|4|* [go-finance](https://github.com/FlashBoys/go-finance) - Comprehensive financial markets data in Go.|
|419|20|2|* [go-money](https://github.com/rhymond/go-money) - Implementation of Fowler's Money pattern.|
|373|20|2|* [accounting](https://github.com/leekchan/accounting) - money and currency formatting for golang.|
|42|2|4|* [vat](https://github.com/dannyvankooten/vat) - VAT number validation & EU VAT rates.|
|39|2|0|* [ofxgo](https://github.com/aclindsa/ofxgo) - Query OFX servers and/or parse the responses (with example command-line client).|
|39|1|0|* [techan](https://github.com/sdcoffey/techan) - Technical analysis library with advanced market analysis and trading strategies.|
|17|2|0|* [transaction](https://github.com/claygod/transaction) - Embedded transactional database of accounts, running in multithreaded mode.|
|12|4|0|* [go-finance](https://github.com/alpeb/go-finance) - Library of financial functions for time value of money (annuities), cash flow, interest rate conversions, bonds and depreciation calculations.|
## Forms

*Libraries for working with forms.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|856|56|5|* [nosurf](https://github.com/justinas/nosurf) - CSRF protection middleware for Go.|
|672|58|8|* [binding](https://github.com/mholt/binding) - Binds form and JSON data from net/http Request to struct.|
|274|43|3|* [gorilla/csrf](https://github.com/gorilla/csrf) - CSRF protection for Go web applications & services.|
|261|11|4|* [form](https://github.com/go-playground/form) - Decodes url.Values into Go value(s) and Encodes Go value(s) into url.Values. Dual Array and Full map support.|
|124|10|1|* [conform](https://github.com/leebenson/conform) - Keeps user input in check. Trims, sanitizes & scrubs data based on struct tags.|
|97|7|2|* [formam](https://github.com/monoculum/formam) - decode form's values into a struct.|
|80|7|2|* [forms](https://github.com/albrow/forms) - Framework-agnostic library for parsing and validating form/JSON data which supports multipart forms and files.|
|19|3|0|* [bind](https://github.com/robfig/bind) - Bind form data to any Go values.|
## Game Development

*Awesome game development libraries.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2074|597|5|* [Leaf](https://github.com/name5566/leaf) - Lightweight game server framework.|
|1373|68|16|* [Pixel](https://github.com/faiface/pixel) - Hand-crafted 2D game library in Go.|
|926|285|0|* [gonet](https://github.com/xtaci/gonet) - Game server skeleton implemented with golang.|
|869|52|7|* [termloop](https://github.com/JoelOtter/termloop) - Terminal-based game engine for Go, built on top of Termbox.|
|864|69|101|* [Ebiten](https://github.com/hajimehoshi/ebiten) - dead simple 2D game library in Go.|
|861|109|11|* [go-sdl2](https://github.com/veandco/go-sdl2) - Go bindings for the [Simple DirectMedia Layer](https://www.libsdl.org/).|
|775|72|31|* [engo](https://github.com/EngoEngine/engo) - Engo is an open-source 2D game engine written in Go. It follows the Entity-Component-System paradigm.|
|610|106|11|* [goworld](https://github.com/xiaonanln/goworld) - Scalable game server engine, featuring space-entity framework and hot-swapping|
|477|19|18|* [Oak](https://github.com/oakmound/oak) - Pure Go game engine.|
|444|51|4|* [nano](https://github.com/lonnng/nano) - Lightweight, facility, high performance golang based game server framework|
|359|23|79|* [Azul3D](https://github.com/azul3d/engine) - 3D game engine written in Go.|
|291|24|4|* [GarageEngine](https://github.com/vova616/GarageEngine) - 2d game engine written in Go working on OpenGL.|
|249|26|0|* [go-astar](https://github.com/beefsack/go-astar) - Go implementation of the A\* path finding algorithm.|
|223|16|7|* [raylib-go](https://github.com/gen2brain/raylib-go) - Go bindings for [raylib](http://www.raylib.com/), a simple and easy-to-use library to learn videogames programming.|
|136|15|0|* [go3d](https://github.com/ungerik/go3d) - Performance oriented 2D/3D math package for Go.|
|77|7|3|* [glop](https://github.com/runningwild/glop) - Glop (Game Library Of Power) is a fairly simple cross-platform game library.|
|11|0|1|* [go-collada](https://github.com/GlenKelley/go-collada) - Go package for working with the Collada file format.|
## Generation and Generics

*Tools to enhance the language with features like generics via code generation.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1436|86|0|* [go-linq](https://github.com/ahmetalpbalkan/go-linq) - .NET LINQ-like query methods for Go.|
|879|66|32|* [gen](https://github.com/clipperhouse/gen) - Code generation tool for ‘generics’-like functionality.|
|683|32|0|* [jennifer](https://github.com/dave/jennifer) - Generate arbitrary Go code without templates.|
|564|18|15|* [goderive](https://github.com/awalterschulze/goderive) - Derives functions from input types.|
|137|5|1|* [interfaces](https://github.com/rjeczalik/interfaces) - Command line tool for generating interface definitions.|
|62|8|0|* [pkgreflect](https://github.com/ungerik/pkgreflect) - Go preprocessor for package scoped reflection.|
|41|3|1|* [go-enum](https://github.com/abice/go-enum) - Code generation for enums from code comments.|
|32|6|1|* [efaceconv](https://github.com/t0pep0/efaceconv) - Code generation tool for high performance conversion from interface{} to immutable type without allocations.|
## Geographic

*Geographic tools and servers*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|4633|223|52|* [Tile38](https://github.com/tidwall/tile38) - Geolocation DB with spatial index and realtime geofencing.|
|620|65|0|* [S2 geometry](https://github.com/golang/geo) - S2 geometry library in Go.|
|82|2|0|* [geocache](https://github.com/melihmucuk/geocache) - In-memory cache that is suitable for geolocation based applications.|
|8|0|0|* [osm](https://github.com/paulmach/osm) - Library for reading, writing and working with OpenStreetMap data and APIs.|
|6|0|0|* [pbf](https://github.com/maguro/pbf) - OpenStreetMap PBF golang encoder/decoder.|
|6|0|0|* [geoserver](https://github.com/hishamkaram/geoserver) - geoserver Is a Go Package For Manipulating a GeoServer Instance via the GeoServer REST API.|
## Go Compilers

*Tools for compiling Go to other languages.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|6804|313|173|* [gopherjs](https://github.com/gopherjs/gopherjs) - Compiler from Go to JavaScript.|
|889|72|22|* [llgo](https://github.com/go-llvm/llgo) - LLVM-based compiler for Go.|
|365|23|3|* [tardisgo](https://github.com/tardisgo/tardisgo) - Golang to Haxe to CPP/CSharp/Java/JavaScript transpiler.|
|4|0|25|* [c4go](https://github.com/Konstantin8105/c4go) - Transpile C code to Go code.|
## Goroutines

*Tools for managing and working with Goroutines.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1951|163|23|* [goworker](https://github.com/benmanns/goworker) - goworker is a Go-based background worker.|
|771|63|2|* [tunny](https://github.com/Jeffail/tunny) - Goroutine pool for golang.|
|367|27|0|* [pool](https://github.com/go-playground/pool) - Limited consumer goroutine or unlimited goroutine pool for easier goroutine handling and cancellation.|
|341|39|2|* [grpool](https://github.com/ivpusic/grpool) - Lightweight Goroutine pool.|
|138|6|1|* [go-floc](https://github.com/workanator/go-floc) - Orchestrate goroutines with ease.|
|75|10|0|* [go-flow](https://github.com/kamildrazkiewicz/go-flow) - Control goroutines execution order.|
|29|4|17|* [semaphore](https://github.com/kamilsk/semaphore) - Semaphore pattern implementation with timeout of lock/unlock operations based on channel and context.|
|29|0|0|* [semaphore](https://github.com/marusama/semaphore) - Fast resizable semaphore implementation based on CAS (faster than channel-based semaphore implementations).|
|21|1|0|* [GoSlaves](https://github.com/themester/GoSlaves) - Simple and Asynchronous Goroutine pool library.|
|15|3|1|* [workerpool](https://github.com/gammazero/workerpool) - Goroutine pool that limits the concurrency of task execution, not the number of tasks queued.|
|14|1|0|* [parallel-fn](https://github.com/rafaeljesus/parallel-fn) - Run functions in parallel.|
|11|2|0|* [worker-pool](https://github.com/vardius/worker-pool) - goworker is a Go simple async worker pool.|
|10|0|0|* [cyclicbarrier](https://github.com/marusama/cyclicbarrier) - CyclicBarrier for golang.|
## GUI

*Libraries for building GUI Applications.*

*Toolkits*

* [go-gtk](http://mattn.github.io/go-gtk/) - Go bindings for GTK.

*Interaction*



|stars|forks|issues|description|
| --- | --- | --- | --- |
|5223|363|67|* [ui](https://github.com/andlabs/ui) - Platform-native GUI library for Go. Cross platform.|
|3947|268|93|* [qt](https://github.com/therecipe/qt) - Qt binding for Go (support for Windows / macOS / Linux / Android / iOS / Sailfish OS / Raspberry Pi).|
|2856|235|26|* [robotgo](https://github.com/go-vgo/robotgo) - Go Native cross-platform GUI system automation. Control the mouse, keyboard and other.|
|2599|420|140|* [walk](https://github.com/lxn/walk) - Windows application library kit for Go.|
|2163|73|6|* [app](https://github.com/murlokswarm/app) - Package to create apps with GO, HTML and CSS. Supports: MacOS, Windows in progress.|
|1828|105|72|* [webview](https://github.com/zserge/webview) - Cross-platform webview window with simple two-way JavaScript bindings (Windows / macOS / Linux).|
|1546|78|8|* [go-astilectron](https://github.com/asticode/go-astilectron) - Build cross platform GUI apps with GO and HTML/JS/CSS (powered by Electron).|
|979|116|21|* [go-sciter](https://github.com/sciter-sdk/go-sciter) - Go bindings for Sciter: the Embeddable HTML/CSS/script engine for modern desktop UI development. Cross platform.|
|424|29|5|* [gosx-notifier](https://github.com/deckarep/gosx-notifier) - OSX Desktop Notifications library for Go.|
|415|78|24|* [gotk3](https://github.com/gotk3/gotk3) - Go bindings for GTK3.|
|413|61|21|* [systray](https://github.com/getlantern/systray) - Cross platform Go library to place an icon and menu in the notification area.|
|121|11|6|* [trayhost](https://github.com/shurcooL/trayhost) - Cross-platform Go library to place an icon in the host operating system's taskbar.|
|105|16|0|* [gowd](https://github.com/dtylman/gowd) - Rapid and simple desktop UI development with GO, HTML, CSS and NW.js. Cross platform.|
## Hardware

*Libraries, tools, and tutorials for interacting with hardware.*

See [go-hardware](https://github.com/rakyll/go-hardware) for a comprehensive list.

## Images

*Libraries for manipulating images.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2197|65|8|* [ln](https://github.com/fogleman/ln) - 3D line art rendering in Go.|
|1803|174|6|* [resize](https://github.com/nfnt/resize) - Image resizing for Go with common interpolation methods.|
|1749|174|36|* [imaginary](https://github.com/h2non/imaginary) - Fast and simple HTTP microservice for image resizing.|
|1726|75|7|* [bild](https://github.com/anthonynsimon/bild) - Collection of image processing algorithms in pure Go.|
|1593|159|1|* [imaging](https://github.com/disintegration/imaging) - Simple Go image processing package.|
|1548|75|4|* [pt](https://github.com/fogleman/pt) - Path tracing engine written in Go.|
|1311|78|11|* [gg](https://github.com/fogleman/gg) - 2D rendering in pure Go.|
|1089|57|5|* [smartcrop](https://github.com/muesli/smartcrop) - Finds good crops for arbitrary images and crop sizes.|
|1064|70|0|* [gift](https://github.com/disintegration/gift) - Package of image processing filters.|
|1035|86|6|* [svgo](https://github.com/ajstarks/svgo) - Go Language Library for SVG generation.|
|947|115|34|* [gocv](https://github.com/hybridgroup/gocv) - Go package for computer vision using OpenCV 3.3+.|
|946|41|2|* [geopattern](https://github.com/pravj/geopattern) - Create beautiful generative image patterns from a string.|
|928|155|37|* [go-opencv](https://github.com/lazywei/go-opencv) - Go bindings for OpenCV.|
|833|75|17|* [picfit](https://github.com/thoas/picfit) - An image resizing server written in Go.|
|729|99|9|* [imagick](https://github.com/gographics/imagick) - Go binding to ImageMagick's MagickWand C API.|
|513|104|60|* [bimg](https://github.com/h2non/bimg) - Small package for fast and efficient image processing using libvips.|
|248|28|1|* [go-nude](https://github.com/koyachi/go-nude) - Nudity detection with Go.|
|237|7|6|* [govatar](https://github.com/o1egl/govatar) - Library and CMD tool for generating funny avatars.|
|146|9|1|* [rez](https://github.com/bamiaux/rez) - Image resizing in pure Go and SIMD.|
|115|5|1|* [img](https://github.com/hawx/img) - Selection of image manipulation tools.|
|86|10|3|* [goimagehash](https://github.com/corona10/goimagehash) - Go Perceptual image hashing package.|
|70|19|2|* [go-cairo](https://github.com/ungerik/go-cairo) - Go binding for the cairo graphics library.|
|42|11|0|* [go-gd](https://github.com/bolknote/go-gd) - Go binding for GD library.|
|23|1|0|* [go-webcolors](https://github.com/jyotiska/go-webcolors) - Port of webcolors library from Python to Go.|
|15|9|1|* [tga](https://github.com/ftrvxmtrx/tga) - Package tga is a TARGA image format decoder/encoder.|
|3|0|1|* [mpo](https://github.com/donatj/mpo) - Decoder and conversion tool for MPO 3D Photos.|
## IoT (Internet of Things)

*Libraries for programming devices of the IoT.*

* [periph](https://periph.io/) - Peripherals I/O to interface with low-level board facilities.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|662|158|41|* [gatt](https://github.com/paypal/gatt) - Gatt is a Go package for building Bluetooth Low Energy peripherals.|
|583|82|63|* [flogo](https://github.com/tibcosoftware/flogo) - Project Flogo is an Open Source Framework for IoT Edge Apps & Integration.|
|465|94|18|* [mainflux](https://github.com/Mainflux/mainflux) - Industrial IoT Messaging and Device Management Server.|
|201|14|9|* [devices](https://github.com/goiot/devices) - Suite of libraries for IoT devices, experimental for x/exp/io.|
|140|23|38|* [sensorbee](https://github.com/sensorbee/sensorbee) - Lightweight stream processing engine for IoT.|
|101|10|16|* [connectordb](https://github.com/connectordb/connectordb) - Open-Source Platform for Quantified Self & IoT.|
|16|3|9|* [eywa](https://github.com/xcodersun/eywa) - Project Eywa is essentially a connection manager that keeps track of connected devices.|
|0|0|0|* [gobot](https://github.com/hybridgroup/gobot/) - Gobot is a framework for robotics, physical computing, and the Internet of Things.|
|0|0|0|* [iot](https://github.com/vaelen/iot/) - IoT is a simple framework for implementing a Google IoT Core device.|
## Logging

*Libraries for generating and working with log files.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|7347|958|164|* [logrus](https://github.com/Sirupsen/logrus) - Structured logger for Go.|
|3853|258|18|* [zap](https://github.com/uber-go/zap) - Fast, structured, leveled logging in Go.|
|2323|148|18|* [spew](https://github.com/davecgh/go-spew) - Implements a deep pretty printer for Go data structures to aid in debugging.|
|1791|384|2|* [glog](https://github.com/golang/glog) - Leveled execution logs for Go.|
|1114|191|32|* [seelog](https://github.com/cihub/seelog) - Logging functionality with flexible dispatching, filtering, and formatting.|
|1079|53|8|* [zerolog](https://github.com/rs/zerolog) - Zero-allocation JSON logger.|
|1058|240|41|* [tail](https://github.com/hpcloud/tail) - Go package striving to emulate the features of the BSD tail program.|
|821|116|14|* [lumberjack](https://github.com/natefinch/lumberjack) - Simple rolling logger, implements io.WriteCloser.|
|733|88|40|* [log15](https://github.com/inconshreveable/log15) - Simple, powerful logging for Go.|
|540|54|17|* [log](https://github.com/apex/log) - Structured logging package for Go.|
|325|34|21|* [logxi](https://github.com/mgutz/logxi) - 12-factor app logger that is fast and makes you happy.|
|246|17|0|* [log](https://github.com/go-playground/log) - Simple, configurable and scalable Structured Logging for Go.|
|211|18|2|* [logutils](https://github.com/hashicorp/logutils) - Utilities for slightly better logging in Go (Golang) extending the standard logger.|
|180|24|4|* [go-logger](https://github.com/apsdehal/go-logger) - Simple logger of Go Programs, with level handlers.|
|121|9|2|* [xlog](https://github.com/rs/xlog) - Structured logger for `net/context` aware HTTP handlers with flexible dispatching.|
|115|13|0|* [logger](https://github.com/azer/logger) - Minimalistic logging library for Go.|
|86|22|8|* [ozzo-log](https://github.com/go-ozzo/ozzo-log) - High performance logging supporting log severity, categorization, and filtering. Can send filtered log messages to various targets (e.g. console, network, mail).|
|75|7|9|* [log-voyage](https://github.com/firstrow/logvoyage) - Full-featured logging saas written in golang.|
|44|4|1|* [stdlog](https://github.com/alexcesaro/log) - Stdlog is an object-oriented library providing leveled logging. It is very useful for cron jobs.|
|34|6|1|* [gologger](https://github.com/sadlil/gologger) - Simple easy to use log lib for go, logs in Colored Console, Simple Console, File or Elasticsearch.|
|32|6|0|* [logex](https://github.com/chzyer/logex) - Golang log lib, supports tracking and level, wrap by standard log lib.|
|26|11|3|* [go-log](https://github.com/ian-kent/go-log) - Log4j implementation in Go.|
|20|11|1|* [logrusly](https://github.com/sebest/logrusly) - [logrus](https://github.com/sirupsen/logrus) plug-in to send errors to a [Loggly](https://www.loggly.com/).|
|17|0|0|* [log](https://github.com/teris-io/log) - Structured log interface for Go cleanly separates logging facade from its implementation.|
|15|8|1|* [go-log](https://github.com/siddontang/go-log) - Log lib supports level and multi handlers.|
|13|11|1|* [mlog](https://github.com/jbrodriguez/mlog) - Simple logging module for go, with 5 levels, an optional rotating logfile feature and stdout/stderr output.|
|11|3|0|* [glg](https://github.com/kpango/glg) - glg is simple and fast leveled logging library for Go.|
|9|0|5|* [gomol](https://github.com/aphistic/gomol) - Multiple-output, structured logging for Go with extensible logging outputs.|
|8|0|0|* [go-cronowriter](https://github.com/utahta/go-cronowriter) - Simple writer that rotate log files automatically based on current date and time, like cronolog.|
|6|3|0|* [distillog](https://github.com/amoghe/distillog) - distilled levelled logging (think of it as stdlib + log levels).|
|5|0|0|* [logdump](https://github.com/ewwwwwqm/logdump) - Package for multi-level logging.|
|4|1|0|* [journald](https://github.com/ssgreg/journald) - Go implementation of systemd Journal's native API for logging.|
|2|0|0|* [logo](https://github.com/mbndr/logo) - Golang logger to different configurable writers.|
|2|0|0|* [xlog](https://github.com/xfxdev/xlog) - Plugin architecture and flexible log system for Go, with level ctrl, multiple log target and custom log format.|
|0|0|0|* [gone/log](https://github.com/One-com/gone/tree/master/log) - Fast, extendable, full-featured, std-lib source compatible log library.|
## Machine Learning

*Libraries for Machine Learning.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|5552|699|50|* [GoLearn](https://github.com/sjwhitworth/golearn) - General Machine Learning library for Go.|
|1875|179|36|* [gorgonia](https://github.com/chewxy/gorgonia) - graph-based computational library like Theano for Go that provides primitives for building various machine learning and neural network algorithms.|
|866|68|5|* [goml](https://github.com/cdipaolo/goml) - On-line Machine Learning in Go.|
|775|41|0|* [tfgo](https://github.com/galeone/tfgo) - Easy to use Tensorflow bindings: simplifies the usage of the official Tensorflow Go bindings. Define computational graphs in Go, load and execute models trained in Python.|
|589|71|33|* [CloudForest](https://github.com/ryanbressler/CloudForest) - Fast, flexible, multi-threaded ensembles of decision trees for machine learning in pure Go.|
|546|86|9|* [bayesian](https://github.com/jbrukh/bayesian) - Naive Bayesian Classification for Golang.|
|496|68|6|* [gosseract](https://github.com/otiai10/gosseract) - Go package for OCR (Optical Character Recognition), by using Tesseract C++ library.|
|480|30|0|* [gago](https://github.com/MaxHalford/gago) - Multi-population, flexible, parallel genetic algorithm.|
|245|36|5|* [gobrain](https://github.com/goml/gobrain) - Neural Networks written in go.|
|205|13|0|* [regommend](https://github.com/muesli/regommend) - Recommendation & collaborative filtering engine.|
|169|7|1|* [go-deep](https://github.com/patrikeh/go-deep) - A feature-rich neural network library in Go.|
|156|38|0|* [go-galib](https://github.com/thoj/go-galib) - Genetic Algorithms library written in Go / golang.|
|114|22|5|* [shield](https://github.com/eaigner/shield) - Bayesian text classifier with flexible tokenizers and storage backends for Go.|
|112|9|0|* [goRecommend](https://github.com/timkaye11/goRecommend) - Recommendation Algorithms library written in Go.|
|94|22|2|* [go-fann](https://github.com/white-pony/go-fann) - Go bindings for Fast Artificial Neural Networks(FANN) library.|
|64|4|0|* [goga](https://github.com/tomcraven/goga) - Genetic algorithm library for Go.|
|56|9|1|* [neural-go](https://github.com/schuyler/neural-go) - Multilayer perceptron network implemented in Go, with training via backpropagation.|
|55|8|1|* [libsvm](https://github.com/datastream/libsvm) - libsvm golang version derived work based on LIBSVM 3.14.|
|50|10|0|* [go-pr](https://github.com/daviddengcn/go-pr) - Pattern recognition package in Go lang.|
|39|4|3|* [neat](https://github.com/jinyeom/neat) - Plug-and-play, parallel Go framework for NeuroEvolution of Augmenting Topologies (NEAT).|
|33|9|0|* [golinear](https://github.com/danieldk/golinear) - liblinear bindings for Go.|
|18|2|0|* [godist](https://github.com/e-dard/godist) - Various probability distributions, and associated methods.|
|13|3|0|* [fonet](https://github.com/Fontinalis/fonet) - A Deep Neural Network library written in Go.|
|13|6|2|* [goscore](https://github.com/asafschers/goscore) - Go Scoring API for PMML.|
|10|0|0|* [go-cluster](https://github.com/e-XpertSolutions/go-cluster) - Go implementation of the k-modes and k-prototypes clustering algorithms.|
|9|1|0|* [Varis](https://github.com/Xamber/Varis) - Golang Neural Network.|
|8|2|4|* [probab](https://github.com/ThePaw/probab) - Probability distribution functions. Bayesian inference. Written in pure Go.|
|3|0|0|* [mlgo](https://github.com/NullHypothesis/mlgo) - This project aims to provide minimalistic machine learning algorithms in Go.|
## Messaging

*Libraries that implement messaging systems.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2872|537|39|* [sarama](https://github.com/Shopify/sarama) - Go library for Apache Kafka.|
|2625|216|10|* [Centrifugo](https://github.com/centrifugal/centrifugo) - Real-time messaging (Websockets or SockJS) server in Go.|
|2571|246|20|* [gorush](https://github.com/appleboy/gorush) - Push notification server using [APNs2](https://github.com/sideshow/apns2) and google [GCM](https://github.com/google/go-gcm).|
|2178|264|24|* [machinery](https://github.com/RichardKnop/machinery) - Asynchronous task queue/job queue based on distributed message passing.|
|2167|343|75|* [go-socket.io](https://github.com/googollee/go-socket.io) - socket.io library for golang, a realtime application framework.|
|1681|500|4|* [gopush-cluster](https://github.com/Terry-Mao/gopush-cluster) - gopush-cluster is a go push server cluster.|
|1641|224|9|* [NATS Go Client](https://github.com/nats-io/nats) - Lightweight and high performance publish-subscribe and distributed queueing messaging system - this is the Go library.|
|1374|127|24|* [mangos](https://github.com/go-mangos/mangos) - Pure go implementation of the Nanomsg ("Scalable Protocols") with transport interoperability.|
|1057|225|13|* [go-nsq](https://github.com/nsqio/go-nsq) - the official Go package for NSQ.|
|972|104|4|* [melody](https://github.com/olahol/melody) - Minimalist framework for dealing with websocket sessions, includes broadcasting and automatic ping/pong handling.|
|968|160|55|* [Uniqush-Push](https://github.com/uniqush/uniqush-push) - Redis backed unified push service for server-side notifications to mobile devices.|
|626|99|21|* [zmq4](https://github.com/pebbe/zmq4) - Go interface to ZeroMQ version 4. Also available for [version 3](https://github.com/pebbe/zmq3) and [version 2](https://github.com/pebbe/zmq2).|
|603|53|21|* [Gollum](https://github.com/trivago/gollum) - A n:m multiplexer that gathers messages from different sources and broadcasts them to a set of destinations.|
|370|27|6|* [golongpoll](https://github.com/jcuga/golongpoll) - HTTP longpoll server library that makes web pub-sub simple.|
|360|43|5|* [EventBus](https://github.com/asaskevich/EventBus) - The lightweight event bus with async compatibility.|
|278|17|5|* [Glue](https://github.com/desertbit/glue) - Robust Go and Javascript Socket Library (Alternative to Socket.io).|
|214|66|22|* [dbus](https://github.com/godbus/dbus) - Native Go bindings for D-Bus.|
|212|9|3|* [Benthos](https://github.com/Jeffail/benthos) - A message streaming bridge between a range of protocols.|
|204|17|1|* [emitter](https://github.com/olebedev/emitter) - Emits events using Go way, with wildcard, predicates, cancellation possibilities and many other good wins.|
|191|28|3|* [pubsub](https://github.com/tuxychandru/pubsub) - Simple pubsub package for go.|
|120|15|5|* [guble](https://github.com/smancke/guble) - Messaging server using push notifications (Google Firebase Cloud Messaging, Apple Push Notification services, SMS) as well as websockets, a REST API, featuring distributed operation and message-persistence.|
|87|10|2|* [oplog](https://github.com/dailymotion/oplog) - Generic oplog/replication system for REST APIs.|
|48|9|0|* [drone-line](https://github.com/appleboy/drone-line) - Sending [Line](https://at.line.me/en) notifications using a binary, docker or Drone CI.|
|38|9|4|* [rabbus](https://github.com/rafaeljesus/rabbus) - A tiny wrapper over amqp exchanges and queues.|
|37|3|0|* [RapidMQ](https://github.com/sybrexsys/RapidMQ) - RapidMQ is a lightweight and reliable library for managing of the local messages queue.|
|32|7|0|* [go-notify](https://github.com/TheCreeper/go-notify) - Native implementation of the freedesktop notification spec.|
|32|4|0|* [goose](https://github.com/ian-kent/goose) - Server Sent Events in Go.|
|29|7|2|* [nsq-event-bus](https://github.com/rafaeljesus/nsq-event-bus) - A tiny wrapper around NSQ topic and channel.|
|18|0|0|* [rabtap](https://github.com/jandelgado/rabtap) - RabbitMQ swiss army knife cli app.|
|14|1|0|* [messagebus](https://github.com/vardius/message-bus) - messagebus is a Go simple async message bus, perfect for using as event bus when doing event sourcing, CQRS, DDD.|
|11|0|0|* [event](https://github.com/agoalofalife/event) - Implementation of the pattern observer.|
|7|0|2|* [go-vitotrol](https://github.com/maxatome/go-vitotrol) - Client library to Viessmann Vitotrol web service.|
|6|1|1|* [gaurun-client](https://github.com/osamingo/gaurun-client) - Gaurun Client written in Go.|
|3|1|0|* [hub](https://github.com/leandro-lugaresi/hub) - A Message/Event Hub for Go applications, using publish/subscribe pattern with support for alias like rabbitMQ exchanges.|
## Miscellaneous

*These libraries were placed here because none of the other categories seemed to fit.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2981|168|32|* [errors](https://github.com/pkg/errors) - Package that provides simple error handling primitives.|
|2609|524|64|* [gopsutil](https://github.com/shirou/gopsutil) - Cross-platform library for retrieving process and system utilization(CPU, Memory, Disks, etc).|
|1983|277|19|* [go.uuid](https://github.com/satori/go.uuid) - Implementation of Universally Unique Identifier (UUID). Supported both creation and parsing of UUIDs.|
|1122|98|7|* [gosms](https://github.com/haxpax/gosms) - Your own local SMS gateway in Go that can be used to send SMS.|
|865|89|27|* [archiver](https://github.com/mholt/archiver) - Library and command for making and extracting .zip and .tar.gz archives.|
|616|49|2|* [go-resiliency](https://github.com/eapache/go-resiliency) - Resiliency patterns for golang.|
|484|67|2|* [go-commons-pool](https://github.com/jolestar/go-commons-pool) - Generic object pool for Golang.|
|467|33|0|* [xstrings](https://github.com/huandu/xstrings) - Collection of useful string functions ported from other languages.|
|450|33|7|* [go-multierror](https://github.com/hashicorp/go-multierror) - Go (golang) package for representing a list of errors as a single error.|
|421|28|18|* [jobs](https://github.com/albrow/jobs) - Persistent and flexible background jobs library.|
|331|76|0|* [base64Captcha](https://github.com/mojocn/base64Captcha) - Base64captch supports digit, number, alphabet, arithmetic, audio and digit-alphabet captcha.|
|323|86|10|* [go-chat-bot](https://github.com/go-chat-bot/bot) - IRC, Slack & Telegram bot written in Go.|
|317|8|0|* [conv](https://github.com/cstockton/go-conv) - Package conv provides fast and intuitive conversions across Go types.|
|287|19|0|* [health](https://github.com/dimiro1/health) - Easy to use, extensible health check library.|
|257|18|1|* [shortid](https://github.com/teris-io/shortid) - Distributed generation of super short, unique, non-sequential, URL friendly IDs.|
|178|24|5|* [slacker](https://github.com/shomali11/slacker) - Easy to use framework to create Slack bots.|
|163|9|0|* [banner](https://github.com/dimiro1/banner) - Add beautiful banners into your Go applications.|
|161|15|3|* [gountries](https://github.com/pariz/gountries) - Package that exposes country and subdivision data.|
|156|12|0|* [wuid](https://github.com/edwingeng/wuid) - An extremely fast unique number generator, 10-135 times faster than UUID.|
|112|9|0|* [gofakeit](https://github.com/brianvoe/gofakeit) - Random data generator written in go.|
|97|12|1|* [stats](https://github.com/go-playground/stats) - Monitors Go MemStats + System stats such as Memory, Swap and CPU and sends via UDP anywhere you want for logging etc...|
|94|1|3|* [go-sarah](https://github.com/oklahomer/go-sarah) - Framework to build bot for desired chat services including LINE, Slack, Gitter and more.|
|90|4|3|* [battery](https://github.com/distatus/battery) - Cross-platform, normalized battery information library.|
|76|23|0|* [antch](https://github.com/antchfx/antch) - A fast, powerful and extensible web crawling & scraping framework.|
|50|6|2|* [bitio](https://github.com/icza/bitio) - Highly optimized bit-level Reader and Writer for Go.|
|50|6|0|* [hanu](https://github.com/sbstjn/hanu) - Framework for writing Slack bots.|
|48|4|0|* [lk](https://github.com/hyperboloide/lk) - A simple licensing library for golang.|
|47|7|0|* [margelet](https://github.com/zhulik/margelet) - Framework for building Telegram bots.|
|42|3|2|* [turtle](https://github.com/hackebrot/turtle) - Emojis for Go.|
|38|11|1|* [healthcheck](https://github.com/etherlabsio/healthcheck) - An opinionated and concurrent health-check HTTP handler for RESTful services.|
|34|2|0|* [indigo](https://github.com/osamingo/indigo) - Distributed unique ID generator of using Sonyflake and encoded by Base58.|
|33|4|1|* [xkg](https://github.com/go-xkg/xkg) - X Keyboard Grabber.|
|29|6|0|* [go-unarr](https://github.com/gen2brain/go-unarr) - Decompression library for RAR, TAR, ZIP and 7z archives.|
|26|15|4|* [browscap_go](https://github.com/digitalcrab/browscap_go) - GoLang Library for [Browser Capabilities Project](http://browscap.org/).|
|21|3|1|* [datacounter](https://github.com/miolini/datacounter) - Go counters for readers/writer/http.ResponseWriter.|
|19|0|0|* [autoflags](https://github.com/artyom/autoflags) - Go package to automatically define command line flags from struct fields.|
|18|1|0|* [captcha](https://github.com/steambap/captcha) - Package captcha provides an easy to use, unopinionated API for captcha generation.|
|15|1|0|* [alice](https://github.com/magic003/alice) - Additive dependency injection container for Golang.|
|12|1|0|* [goid](https://github.com/jakehl/goid) - Generate and Parse RFC4122 compliant V4 UUIDs.|
|9|0|0|* [persian](https://github.com/mavihq/persian) - Some utilities for Persian language in go.|
|8|0|0|* [pdfgen](https://github.com/hyperboloide/pdfgen) - HTTP service to generate PDF from Json requests.|
|6|0|0|* [secdl](https://github.com/xor-gate/secdl) - Lighttpd ModSecDownload algorithm ported to go to secure download urls.|
|5|1|0|* [werr](https://github.com/txgruppi/werr) - Error Wrapper creates an wrapper for the error type in Go which captures the File, Line and Stack of where it was called.|
|5|0|0|* [avgRating](https://github.com/kirillDanshin/avgRating) - Calculate average score and rating based on Wilson Score Equation.|
|4|1|0|* [uuid](https://github.com/agext/uuid) - Generate, encode, and decode UUIDs v1 with fast or cryptographic-quality random node identifier.|
|3|0|0|* [hostutils](https://github.com/Wing924/hostutils) - A golang library for packing and unpacking FQDNs list.|
|2|0|0|* [anagent](https://github.com/mudler/anagent) - Minimalistic, pluggable Golang evloop/timer handler with dependency-injection.|
|1|0|0|* [shellwords](https://github.com/Wing924/shellwords) - A Golang library to manipulate strings according to the word parsing rules of the UNIX Bourne shell.|
|0|0|0|* [VarHandler](https://github.com/azr/generators/tree/master/varhandler) - Generate boilerplate http input and ouput handling.|
|0|0|0|* [go-openapi](https://github.com/go-openapi) - Collection of packages to parse and utilize open-api schemas.|
## Natural Language Processing

*Libraries for working with human languages.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|852|31|4|* [when](https://github.com/olebedev/when) - Natural EN and RU language date/time parser with pluggable rules.|
|567|28|4|* [prose](https://github.com/jdkato/prose) - Library for text processing that supports tokenization, part-of-speech tagging, named-entity extraction, and more.|
|527|99|22|* [gojieba](https://github.com/yanyiwu/gojieba) - This is a Go implementation of [jieba](https://github.com/fxsjy/jieba) which a Chinese word splitting algorithm.|
|375|26|1|* [gse](https://github.com/go-ego/gse) - Go efficient text segmentation; support english, chinese, japanese and other.|
|330|20|4|* [nlp](https://github.com/Shixzie/nlp) - Extract values from strings and fill your structs with nlp.|
|276|16|2|* [whatlanggo](https://github.com/abadojack/whatlanggo) - Natural language detection package for Go. Supports 84 languages and 24 scripts (writing systems e.g. Latin, Cyrillic, etc).|
|232|16|3|* [sentences](https://github.com/neurosnap/sentences) - Sentence tokenizer:  converts text into a list of sentences.|
|130|13|0|* [nlp](https://github.com/james-bowman/nlp) - Go Natural Language Processing library supporting LSA (Latent Semantic Analysis).|
|74|10|0|* [go-nlp](https://github.com/nuance/go-nlp) - Utilities for working with discrete probability distributions and other tools useful for doing NLP work.|
|58|17|2|* [gounidecode](https://github.com/fiam/gounidecode) - Unicode transliterator (also known as unidecode) for Go.|
|56|8|0|* [textcat](https://github.com/pebbe/textcat) - Go package for n-gram based text categorization, with support for utf-8 and raw text.|
|54|11|0|* [MMSEGO](https://github.com/awsong/MMSEGO) - This is a GO implementation of [MMSEG](http://technology.chtsai.org/mmseg/) which a Chinese word splitting algorithm.|
|44|12|0|* [go-stem](https://github.com/agonopol/go-stem) - Implementation of the porter stemming algorithm.|
|40|2|0|* [stemmer](https://github.com/dchest/stemmer) - Stemmer packages for Go programming language. Includes English and German stemmers.|
|38|6|3|* [segment](https://github.com/blevesearch/segment) - Go library for performing Unicode Text Segmentation as described in [Unicode Standard Annex #29](http://www.unicode.org/reports/tr29/)|
|31|2|0|* [porter2](https://github.com/zhenjl/porter2) - Really fast Porter 2 stemmer.|
|30|3|1|* [RAKE.go](https://github.com/Obaied/RAKE.go) - Go port of the Rapid Automatic Keyword Extraction Algorithm (RAKE).|
|28|2|0|* [go2vec](https://github.com/danieldk/go2vec) - Reader and utility functions for word2vec embeddings.|
|24|5|1|* [go-unidecode](https://github.com/mozillazg/go-unidecode) - ASCII transliterations of Unicode text.|
|22|4|2|* [paicehusk](https://github.com/rookii/paicehusk) - Golang implementation of the Paice/Husk Stemming Algorithm.|
|19|2|1|* [snowball](https://github.com/goodsign/snowball) - Snowball stemmer port (cgo wrapper) for Go. Provides word stem extraction functionality [Snowball native](http://snowball.tartarus.org/).|
|16|2|2|* [icu](https://github.com/goodsign/icu) - Cgo binding for icu4c C library detection and conversion functions. Guaranteed compatibility with version 50.1.|
|15|1|0|* [go-mystem](https://github.com/dveselov/mystem) - CGo bindings to Yandex.Mystem - russian morphology analyzer.|
|14|5|0|* [golibstemmer](https://github.com/rjohnsondev/golibstemmer) - Go bindings for the snowball libstemmer library including porter 2.|
|11|0|0|* [petrovich](https://github.com/striker2000/petrovich) - Petrovich is the library which inflects Russian names to given grammatical case.|
|10|1|0|* [getlang](https://github.com/rylans/getlang) - Fast natural language detection package.|
|9|6|0|* [libtextcat](https://github.com/goodsign/libtextcat) - Cgo binding for libtextcat C library. Guaranteed compatibility with version 2.2.|
|7|0|0|* [porter](https://github.com/a2800276/porter) - This is a fairly straightforward port of Martin Porter's C implementation of the Porter stemming algorithm.|
|6|0|0|* [shamoji](https://github.com/osamingo/shamoji) - The shamoji is word filtering package written in Go.|
|3|1|2|* [go-eco](https://github.com/ThePaw/go-eco) - Similarity, dissimilarity and distance matrices; diversity, equitability and inequality measures; species richness estimators; coenocline models.|
|0|0|0|* [go-i18n](https://github.com/nicksnyder/go-i18n/) - Package and an accompanying tool to work with localized text.|
|0|0|0|* [dpar](https://github.com/danieldk/dpar/) - Transition-based statistical dependency parser.|
## Networking

*Libraries for working with various layers of the network.*

* [mqttPaho](https://eclipse.org/paho/clients/golang/) - The Paho Go Client provides an MQTT client library for connection to MQTT brokers via TCP, TLS or WebSockets.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|7981|1625|96|* [kcptun](https://github.com/xtaci/kcptun) - Extremely simple & fast udp tunnel based on KCP protocol.|
|6203|551|159|* [fasthttp](https://github.com/valyala/fasthttp) - Package fasthttp is a fast HTTP implementation for Go, up to 10 times faster than net/http.|
|2810|499|38|* [dns](https://github.com/miekg/dns) - Go library for working with DNS.|
|1896|361|62|* [gopacket](https://github.com/google/gopacket) - Go library for packet processing with libpcap bindings.|
|1283|230|49|* [gobgp](https://github.com/osrg/gobgp) - BGP implemented in the Go Programming Language.|
|1187|257|17|* [kcp-go](https://github.com/xtaci/kcp-go) - KCP - Fast and Reliable ARQ Protocol.|
|725|67|14|* [ssh](https://github.com/gliderlabs/ssh) - Higher-level API for building SSH servers (wraps crypto/ssh).|
|504|158|14|* [sftp](https://github.com/pkg/sftp) - Package sftp implements the SSH File Transfer Protocol as described in https://filezilla-project.org/specs/draft-ietf-secsh-filexfer-02.txt.|
|492|48|34|* [go-getter](https://github.com/hashicorp/go-getter) - Go library for downloading files or directories from various sources using a URL.|
|429|37|25|* [NFF-Go](https://github.com/intel-go/nff-go) - Framework for rapid development of performant network functions for cloud and bare-metal (former YANFF).|
|414|81|31|* [mdns](https://github.com/hashicorp/mdns) - Simple mDNS (Multicast DNS) client/server library in Golang.|
|411|96|8|* [water](https://github.com/songgao/water) - Simple TUN/TAP library.|
|403|81|3|* [lhttp](https://github.com/fanux/lhttp) - Powerful websocket framework, build your IM server more easily.|
|342|139|14|* [ftp](https://github.com/jlaffaye/ftp) - Package ftp implements a FTP client as described in [RFC 959](http://tools.ietf.org/html/rfc959).|
|326|130|6|* [gotcp](https://github.com/gansidui/gotcp) - Go package for quickly writing tcp applications.|
|316|31|8|* [grab](https://github.com/cavaliercoder/grab) - Go package for managing file downloads.|
|309|96|3|* [gosnmp](https://github.com/soniah/gosnmp) - Native Go library for performing SNMP actions.|
|308|121|7|* [gopcap](https://github.com/akrennmair/gopcap) - Go wrapper for libpcap.|
|298|24|47|* [fortio](https://github.com/istio/fortio) - Load testing library and command line tool and web UI. Allows to specify a set query-per-second load and record latency histograms and other useful stats and graph them.|
|265|12|1|* [cidranger](https://github.com/yl2chen/cidranger) - Fast IP to CIDR lookup for Go.|
|260|8|1|* [peerdiscovery](https://github.com/schollz/peerdiscovery) - Pure Go library for cross-platform local peer discovery using UDP multicast|
|226|40|7|* [go-stun](https://github.com/ccding/go-stun) - Go implementation of the STUN client (RFC 3489 and RFC 5389).|
|201|26|5|* [raw](https://github.com/mdlayher/raw) - Package raw enables reading and writing data at the device driver level for a network interface.|
|196|20|1|* [buffstreams](https://github.com/stabbycutyou/buffstreams) - Streaming protocolbuffer data over TCP made easy.|
|184|73|1|* [tcp_server](https://github.com/firstrow/tcp_server) - Go library for building tcp servers faster.|
|154|50|12|* [winrm](https://github.com/masterzen/winrm) - Go WinRM client to remotely execute commands on Windows machines.|
|140|11|0|* [ethernet](https://github.com/mdlayher/ethernet) - Package ethernet implements marshaling and unmarshaling of IEEE 802.3 Ethernet II frames and IEEE 802.1Q VLAN tags.|
|137|22|3|* [utp](https://github.com/anacrolix/utp) - Go uTP micro transport protocol implementation.|
|132|23|0|* [arp](https://github.com/mdlayher/arp) - Package arp implements the ARP protocol, as described in RFC 826.|
|103|27|39|* [canopus](https://github.com/zubairhamed/canopus) - CoAP Client/Server implementation (RFC 7252).|
|99|13|9|* [sslb](https://github.com/eduardonunesp/sslb) - It's a Super Simples Load Balancer, just a little project to achieve some kind of performance.|
|88|11|1|* [stun](https://github.com/go-rtc/stun) - Go implementation of RFC 5389 STUN protocol.|
|79|7|3|* [jazigo](https://github.com/udhos/jazigo) - Jazigo is a tool written in Go for retrieving configuration for multiple network devices.|
|47|1|0|* [ether](https://github.com/songgao/ether) - Cross-platform Go package for sending and receiving ethernet frames.|
|47|12|2|* [dhcp6](https://github.com/mdlayher/dhcp6) - Package dhcp6 implements a DHCPv6 server, as described in RFC 3315.|
|38|7|0|* [xtcp](https://github.com/xfxdev/xtcp) - TCP Server Framework with simultaneous full duplex communication,graceful shutdown,custom protocol.|
|34|6|0|* [portproxy](https://github.com/aybabtme/portproxy) - Simple TCP proxy which adds CORS support to API's which don't support it.|
|33|3|0|* [linkio](https://github.com/ian-kent/linkio) - Network link speed simulation for Reader/Writer interfaces.|
|18|5|1|* [graval](https://github.com/koofr/graval) - Experimental FTP server framework.|
|13|2|0|* [publicip](https://github.com/polera/publicip) - Package publicip returns your public facing IPv4 address (internet egress).|
|11|2|0|* [golibwireshark](https://github.com/sunwxg/golibwireshark) - Package golibwireshark use libwireshark library to decode pcap file and analyse dissection data.|
|6|2|0|* [goshark](https://github.com/sunwxg/goshark) - Package goshark use tshark to decode IP packet and create data struct to analyse packet.|
|5|0|0|* [llb](https://github.com/kirillDanshin/llb) - It's a very simple but quick backend for proxy servers. Can be useful for fast redirection to predefined domain with zero memory allocation and fast response.|
## OpenGL

*Libraries for using OpenGL in Go.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|475|61|6|* [glfw](https://github.com/go-gl/glfw) - Go bindings for GLFW 3.|
|474|37|7|* [gl](https://github.com/go-gl/gl) - Go bindings for OpenGL (generated via glow).|
|226|32|10|* [mathgl](https://github.com/go-gl/mathgl) - Pure Go math package specialized for 3D math, with inspiration from GLM.|
|115|10|5|* [goxjs/gl](https://github.com/goxjs/gl) - Go cross-platform OpenGL bindings (OS X, Linux, Windows, browsers, iOS, Android).|
|51|11|7|* [goxjs/glfw](https://github.com/goxjs/glfw) - Go cross-platform glfw library for creating an OpenGL context and receiving events.|
## ORM

*Libraries that implement Object-Relational Mapping or datamapping techniques.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|8879|1042|115|* [GORM](https://github.com/jinzhu/gorm) - The fantastic ORM library for Golang, aims to be developer friendly.|
|3183|439|159|* [Xorm](https://github.com/go-xorm/xorm) - Simple and powerful ORM for Go.|
|2767|325|116|* [gorp](https://github.com/go-gorp/gorp) - Go Relational Persistence, ORM-ish library for Go.|
|1659|117|18|* [go-pg](https://github.com/go-pg/pg) - PostgreSQL ORM with focus on PostgreSQL specific features and performance.|
|1209|98|64|* [upper.io/db](https://github.com/upper/db) - Single interface for interacting with different data sources through the use of adapters that wrap mature database drivers.|
|1160|108|50|* [SQLBoiler](https://github.com/volatiletech/sqlboiler) - ORM generator. Generate a featureful and blazing-fast ORM tailored to your database schema.|
|641|28|51|* [reform](https://github.com/go-reform/reform) - Better ORM for Go, based on non-empty interfaces and code generation.|
|565|98|0|* [pop/soda](https://github.com/markbates/pop) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.|
|493|87|9|* [QBS](https://github.com/coocood/qbs) - Stands for Query By Struct. A Go ORM.|
|299|14|9|* [go-queryset](https://github.com/jirfag/go-queryset) - 100% type-safe ORM with code generation and MySQL, PostgreSQL, Sqlite3, SQL Server support based on GORM.|
|201|12|2|* [Zoom](https://github.com/albrow/zoom) - Blazing-fast datastore and querying engine built on Redis.|
|88|8|0|* [go-store](https://github.com/gosuri/go-store) - Simple and fast Redis backed key-value store library for Go.|
|60|7|1|* [gomodel](https://github.com/cosiner/gomodel) - Lightweight, fast, orm-like library helps interactive with database.|
|36|8|0|* [go-sqlbuilder](https://github.com/huandu/go-sqlbuilder) - A flexible and powerful SQL string builder library plus a zero-config ORM.|
|27|1|3|* [Marlow](https://github.com/dadleyy/marlow) - Generated ORM from project structs for compile time safety assurances.|
|10|2|0|* [grimoire](https://github.com/Fs02/grimoire) - Grimoire is a database access layer and validation for golang. (Support: MySQL, PostgreSQL and SQLite3).|
|3|0|0|* [lore](https://github.com/abrahambotros/lore) - Simple and lightweight pseudo-ORM/pseudo-struct-mapping environment for Go.|
|0|0|0|* [beego orm](https://github.com/astaxie/beego/tree/master/orm) - Powerful orm framework for go. Support: pq/mysql/sqlite3.|
## Package Management

*Libraries for package and dependency management.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|8982|637|385|* [dep](https://github.com/golang/dep) - Go dependency tool.|
|6621|441|376|* [glide](https://github.com/Masterminds/glide) - Manage your golang vendor and vendored packages with ease. Inspired by tools like Maven, Bundler, and Pip.|
|5349|467|79|* [godep](https://github.com/tools/godep) - dependency tool for go, godep helps build packages reproducibly by fixing their dependencies.|
|3387|260|115|* [govendor](https://github.com/kardianos/govendor) - Go Package Manager. Go vendor tool that works with the standard vendor file.|
|1746|144|45|* [gopm](https://github.com/gpmgo/gopm) - Go Package Manager.|
|1313|93|15|* [gom](https://github.com/mattn/gom) - Go Manager - bundle for go.|
|1200|54|14|* [gpm](https://github.com/pote/gpm) - Barebones dependency manager for Go.|
|774|46|30|* [goop](https://github.com/nitrous-io/goop) - Simple dependency manager for Go (golang), inspired by Bundler.|
|739|74|44|* [gvt](https://github.com/FiloSottile/gvt) - `gvt` is a simple vendoring tool made for Go native vendoring (aka GO15VENDOREXPERIMENT), based on gb-vendor.|
|249|10|14|* [nut](https://github.com/jingweno/nut) - Vendor Go dependencies.|
|214|6|3|* [johnny-deps](https://github.com/VividCortex/johnny-deps) - Minimal dependency version using Git.|
|193|10|4|* [gigo](https://github.com/LyricalSecurity/gigo) - PIP-like dependency tool for golang, with support for private repositories and hashes.|
|109|6|3|* [VenGO](https://github.com/DamnWidget/VenGO) - create and manage exportable isolated go virtual environments.|
|40|7|9|* [gop](https://github.com/lunny/gop) - Build and manage your Go applications out of GOPATH|
## Query Language


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2994|273|78|* [graphql-go](https://github.com/graphql-go/graphql) - Implementation of GraphQL for Go.|
|1471|139|62|* [graphql](https://github.com/neelance/graphql-go) - GraphQL server with a focus on ease of use.|
|148|17|2|* [jsonql](https://github.com/elgs/jsonql) - JSON query expression library in Golang.|
|45|5|2|* [graphql](https://github.com/tmc/graphql) - graphql parser + utilities.|
|34|1|2|* [graphql](https://github.com/sevki/graphql) - GraphQL implementation in go.|
## Resource Embedding


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1290|82|35|* [go.rice](https://github.com/GeertJohan/go.rice) - go.rice is a Go package that makes working with resources such as html,js,css,images and templates very easy.|
|1283|73|12|* [statik](https://github.com/rakyll/statik) - Embeds static files into a Go executable.|
|867|26|6|* [packr](https://github.com/gobuffalo/packr) - The simple and easy way to embed static files into Go binaries.|
|299|46|6|* [esc](https://github.com/mjibson/esc) - Embeds files into Go programs and provides http.FileSystem interfaces to them.|
|293|19|7|* [vfsgen](https://github.com/shurcooL/vfsgen) - Generates a vfsdata.go file that statically implements the given virtual filesystem.|
|241|19|3|* [fileb0x](https://github.com/UnnoTed/fileb0x) - Simple tool to embed files in go with focus on "customization" and ease to use.|
|145|12|0|* [go-resources](https://github.com/omeid/go-resources) - Unfancy resources embedding with Go.|
|48|3|0|* [statics](https://github.com/go-playground/statics) - Embeds static resources into go files for single binary compilation + works with http.FileSystem + symlinks.|
|12|2|0|* [go-embed](https://github.com/pyros2097/go-embed) - Generates go code to embed resource files into your library or executable.|
|11|2|2|* [templify](https://github.com/wlbr/templify) - Embed external template files into Go code to create single file binaries.|
## Science and Data Analysis

*Libraries for scientific computing and data analyzing.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1308|113|49|* [streamtools](https://github.com/nytlabs/streamtools) - general purpose, graphical tool for dealing with streams of data.|
|1074|68|0|* [gosl](https://github.com/cpmech/gosl) - Go scientific library for linear algebra, FFT, geometry, NURBS, numerical methods, probabilities, optimisation, differential equations, and more.|
|881|64|10|* [stats](https://github.com/montanaflynn/stats) - Statistics package with common functions missing from the Golang standard library.|
|824|78|76|* [gonum/plot](https://github.com/gonum/plot) - gonum/plot provides an API for building and drawing plots in Go.|
|522|45|6|* [go-dsp](https://github.com/mjibson/go-dsp) - Digital Signal Processing for Go.|
|481|66|3|* [goraph](https://github.com/gyuho/goraph) - Pure Go graph theory library(data structure, algorith visualization).|
|481|77|4|* [chart](https://github.com/vdobler/chart) - Simple Chart Plotting library for Go. Supports many graphs types.|
|461|51|20|* [gonum/mat64](https://github.com/gonum/matrix) - The general purpose package for matrix computation. Package mat64 provides basic linear algebra operations for float64 matrices.|
|303|64|11|* [go.matrix](https://github.com/skelterjohn/go.matrix) - linear algebra for go (has been stalled).|
|219|17|2|* [ewma](https://github.com/VividCortex/ewma) - Exponentially-weighted moving averages.|
|139|6|0|* [graph](https://github.com/yourbasic/graph) - Library of basic graph algorithms.|
|117|17|1|* [blas](https://github.com/ziutek/blas) - Implementation of BLAS (Basic Linear Algebra Subprograms).|
|105|17|3|* [gohistogram](https://github.com/VividCortex/gohistogram) - Approximate histograms for data streams.|
|59|8|2|* [vectormath](https://github.com/spate/vectormath) - Vectormath for Go, an adaptation of the scalar C functions from Sony's Vector Math library, as found in the Bullet-2.79 source code (currently inactive).|
|36|10|1|* [pagerank](https://github.com/alixaxel/pagerank) - Weighted PageRank algorithm implemented in Go.|
|35|12|1|* [geom](https://github.com/skelterjohn/geom) - 2D geometry for golang.|
|31|8|7|* [evaler](https://github.com/soniah/evaler) - Simple floating point arithmetic expression evaluator.|
|29|6|0|* [sparse](https://github.com/james-bowman/sparse) - Go Sparse matrix formats for linear algebra supporting scientific and machine learning applications, compatible with gonum matrix libraries.|
|24|9|4|* [gostat](https://github.com/ematvey/gostat) - Statistics library for the go language.|
|18|6|1|* [orb](https://github.com/paulmach/orb) - 2D geometry types with clipping, GeoJSON and Mapbox Vector Tile support.|
|9|2|0|* [TextRank](https://github.com/DavidBelicza/TextRank) - TextRank implementation in Golang with extendable features (summarization, weighting, phrase extraction) and multithreading (goroutine) support.|
|7|1|5|* [go-fn](https://github.com/ematvey/go-fn) - Mathematical functions written in Go language, that are not covered by math pkg.|
|6|3|0|* [gofrac](https://github.com/anschelsc/gofrac) - (goinstallable) fractions library for go with support for basic arithmetic.|
|5|0|1|* [ode](https://github.com/ChristopherRabotin/ode) - Ordinary differential equation (ODE) solver which supports extended states and channel-based iteration stop conditions.|
|4|1|0|* [goent](https://github.com/kzahedi/goent) - GO Implementation of Entropy Measures|
|3|0|0|* [PiHex](https://github.com/claygod/PiHex) - Implementation of the "Bailey-Borwein-Plouffe" algorithm for the hexadecimal number Pi.|
|3|0|3|* [go-gt](https://github.com/ThePaw/go-gt) - Graph theory algorithms written in "Go" language.|
|3|0|0|* [gocomplex](https://github.com/varver/gocomplex) - Complex number library for the Go programming language.|
## Security

*Libraries that are used to help make your application more secure.*

* [autocert](https://godoc.org/golang.org/x/crypto/acme/autocert) - Auto provision Let's Encrypt certificates and start a TLS server.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|2549|305|112|* [lego](https://github.com/xenolf/lego) - Pure Go ACME client library and CLI tool (for use with Let's Encrypt).|
|1514|80|68|* [acmetool](https://github.com/hlandau/acme) - ACME (Let's Encrypt) client tool with automatic renewal.|
|1317|142|4|* [Cameradar](https://github.com/Ullaakut/cameradar) - Tool and library to remotely hack RTSP streams from surveillance cameras.|
|954|48|0|* [secure](https://github.com/unrolled/secure) - HTTP middleware for Go that facilitates some quick security wins.|
|765|22|1|* [memguard](https://github.com/awnumar/memguard) - A pure Go library for handling sensitive values in memory.|
|352|16|2|* [nacl](https://github.com/kevinburke/nacl) - Go implementation of the NaCL set of API's.|
|219|5|0|* [BadActor](https://github.com/jaredfolkins/badactor) - In-memory, application-driven jailer built in the spirit of fail2ban.|
|181|12|4|* [passlib](https://github.com/hlandau/passlib) - Futureproof password hashing library.|
|144|13|7|* [ssh-vault](https://github.com/ssh-vault/ssh-vault) - encrypt/decrypt using ssh keys.|
|129|15|1|* [simple-scrypt](https://github.com/elithrar/simple-scrypt) - Scrypt package with a simple, obvious API and automatic cost calibration built-in.|
|78|29|2|* [go-yara](https://github.com/hillu/go-yara) - Go Bindings for [YARA](https://github.com/plusvic/yara), the "pattern matching swiss knife for malware researchers (and everyone else)".|
|59|1|0|* [argon2pw](https://github.com/raja/argon2pw) - Argon2 password hash generation with constant-time password comparison.|
|15|5|0|* [goSecretBoxPassword](https://github.com/dwin/goSecretBoxPassword) - A probably paranoid package for securely hashing and encrypting passwords.|
## Serialization

*Libraries and tools for binary serialization.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2884|664|54|* [goprotobuf](https://github.com/golang/protobuf) - Go support, in the form of a library and protocol compiler plugin, for Google's protocol buffers.|
|2771|234|11|* [jsoniter](https://github.com/json-iterator/go) - High-performance 100% compatible drop-in replacement of "encoding/json".|
|2156|183|21|* [structs](https://github.com/fatih/structs) - Library with support for converting structs to maps, struct keys/values to slices, and more.|
|1656|229|52|* [gogoprotobuf](https://github.com/gogo/protobuf) - Protocol Buffers for Go with Gadgets.|
|1402|177|26|* [mapstructure](https://github.com/mitchellh/mapstructure) - Go library for decoding generic map values into native Go structures.|
|934|144|1|* [go-codec](https://github.com/ugorji/go) - High Performance, feature-Rich, idiomatic encode, decode and rpc library for msgpack, cbor and json, with runtime-based OR code-generation support.|
|364|28|10|* [colfer](https://github.com/pascaldekloe/colfer) - Code generation for the Colfer binary format.|
|259|19|0|* [go-capnproto](https://github.com/glycerine/go-capnproto) - Cap'n Proto library and parser for go.|
|209|6|1|* [csvutil](https://github.com/jszwec/csvutil) - High Performance, idiomatic CSV record encoding and decoding to native Go structures.|
|84|30|2|* [php_session_decoder](https://github.com/yvasiyarov/php_session_decoder) - GoLang library for working with PHP session format and PHP Serialize/Unserialize functions.|
|70|6|0|* [structomap](https://github.com/tuvistavie/structomap) - Library to easily and dynamically generate maps from static structures.|
|58|8|3|* [bambam](https://github.com/glycerine/bambam) - generator for Cap'n Proto schemas from go.|
|27|10|7|* [asn1](https://github.com/PromonLogicalis/asn1) - Asn.1 BER and DER encoding library for golang.|
|3|0|0|* [fwencoder](https://github.com/o1egl/fwencoder) - Fixed width file parser (encoding and decoding library) for Go.|
## Server Applications

* [consul](https://www.consul.io/) - Consul is a tool for service discovery, monitoring and configuration.
* [nsq](http://nsq.io/) - A realtime distributed messaging platform.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|18286|3605|261|* [etcd](https://github.com/coreos/etcd) - Highly-available key value store for shared configuration and service discovery.|
|17094|1303|108|* [Caddy](https://github.com/mholt/caddy) - Caddy is an alternative, HTTP/2 web server that's easy to configure and use.|
|11320|953|116|* [minio](https://github.com/minio/minio) - Minio is a distributed object storage server.|
|2536|110|10|* [devd](https://github.com/cortesi/devd) - Local webserver for developers.|
|435|27|0|* [algernon](https://github.com/xyproto/algernon) - HTTP/2 web server with built-in support for Lua, Markdown, GCSS and Amber.|
|393|16|9|* [jackal](https://github.com/ortuman/jackal) - An XMPP server written in Go.|
|340|12|3|* [Flagr](https://github.com/checkr/flagr) - Flagr is an open-source feature flagging and A/B testing service.|
|289|23|14|* [Fider](https://github.com/getfider/fider) - Fider is an open platform to collect and organize customer feedback.|
|23|4|0|* [yakvs](https://github.com/sci4me/yakvs) - Small, networked, in-memory key-value store.|
## Template Engines

*Libraries and tools for templating and lexing.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2334|187|31|* [gofpdf](https://github.com/jung-kurt/gofpdf) - PDF document generator with high level support for text, drawing and images.|
|1206|118|40|* [pongo2](https://github.com/flosch/pongo2) - Django-like template-engine for Go.|
|963|62|14|* [quicktemplate](https://github.com/valyala/quicktemplate) - Fast, powerful, yet easy to use template engine. Converts templates into Go code and then compiles it.|
|955|56|18|* [hero](https://github.com/shiyanhui/hero) - Hero is a handy, fast and powerful go template engine.|
|926|143|33|* [mustache](https://github.com/hoisie/mustache) - Go implementation of the Mustache template language.|
|784|47|17|* [amber](https://github.com/eknkc/amber) - Amber is an elegant templating engine for Go Programming Language It is inspired from HAML and Jade.|
|715|33|31|* [ace](https://github.com/yosssi/ace) - Ace is an HTML template engine for Go, inspired by Slim and Jade. Ace is a refinement of Gold.|
|628|78|10|* [Razor](https://github.com/sipin/gorazor) - Razor view engine for Golang.|
|458|29|21|* [jet](https://github.com/CloudyKit/jet) - Jet template engine.|
|370|27|10|* [ego](https://github.com/benbjohnson/ego) - Lightweight templating language that lets you write templates in Go. Templates are translated into Go and compiled.|
|262|29|8|* [raymond](https://github.com/aymerick/raymond) - Complete handlebars implementation in Go.|
|183|28|3|* [fasttemplate](https://github.com/valyala/fasttemplate) - Simple and fast template engine. Substitutes template placeholders up to 10x faster than [text/template](http://golang.org/pkg/text/template/).|
|124|21|4|* [Soy](https://github.com/robfig/soy) - Closure templates (aka Soy templates) for Go, following the [official spec](https://developers.google.com/closure/templates/).|
|74|2|3|* [grender](https://github.com/dannyvankooten/grender) - small wrapper around html/template for file-based templates that support extending other template files.|
|69|4|2|* [kasia.go](https://github.com/ziutek/kasia.go) - Templating system for HTML and other text documents - go implementation.|
|58|3|2|* [velvet](https://github.com/gobuffalo/velvet) - Complete handlebars implementation in Go.|
|51|5|4|* [liquid](https://github.com/osteele/liquid) - Go implementation of Shopify Liquid templates.|
|19|2|1|* [damsel](https://github.com/dskinner/damsel) - Markup language featuring html outlining via css-selectors, extensible via pkg html/template and others.|
## Testing

*Libraries for testing codebases and generating test data.*

* Testing Frameworks
    * [ginkgo](http://onsi.github.io/ginkgo/) - BDD Testing Framework for Go.
    * [gocheck](http://labix.org/gocheck) - More advanced testing framework alternative to gotest.
    * [gomega](http://onsi.github.io/gomega/) - Rspec like matcher/assertion library.

* Mock

* Fuzzing and delta-debugging/reducing/shrinking.

* Selenium and browser control tools.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|4956|494|117|    * [Testify](https://github.com/stretchr/testify) - Sacred extension to the standard go testing package.|
|2227|125|22|    * [go-fuzz](https://github.com/dvyukov/go-fuzz) - Randomized testing system.|
|1989|124|36|    * [chromedp](https://github.com/knq/chromedp) - a way to drive/test Chrome, Safari, Edge, Android Webviews, and other browsers supporting the Chrome Debugging Protocol.|
|1340|164|38|    * [gomock](https://github.com/golang/mock) - Mocking framework for the Go programming language.|
|872|58|10|    * [httpexpect](https://github.com/gavv/httpexpect) - Concise, declarative, and easy to use end-to-end HTTP and REST API testing.|
|825|101|5|    * [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock) - Mock SQL driver for testing database interactions.|
|493|12|6|    * [baloo](https://github.com/h2non/baloo) - Expressive and versatile end-to-end HTTP API testing made easy.|
|488|37|9|    * [goblin](https://github.com/franela/goblin) - Mocha like testing framework fo Go.|
|474|21|8|    * [gock](https://github.com/h2non/gock) - Versatile HTTP mocking made easy.|
|422|38|5|    * [gofuzz](https://github.com/google/gofuzz) - Library for populating go objects with random values.|
|382|43|14|    * [godog](https://github.com/DATA-DOG/godog) - Cucumber or Behat like BDD framework for Go.|
|235|36|19|    * [counterfeiter](https://github.com/maxbrunsfeld/counterfeiter) - Tool for generating self-contained mock objects.|
|226|19|11|    * [frisby](https://github.com/verdverm/frisby) - REST API testing framework.|
|196|17|4|    * [go-vcr](https://github.com/dnaeon/go-vcr) - Record and replay your HTTP interactions for fast, deterministic and accurate tests.|
|186|8|53|    * [Tavor](https://github.com/zimmski/tavor) - Generic fuzzing and delta-debugging framework.|
|178|5|0|    * [go-carpet](https://github.com/msoap/go-carpet) - Tool for viewing test coverage in terminal.|
|170|12|5|    * [testfixtures](https://github.com/go-testfixtures/testfixtures) - A helper for Rails' like test fixtures to test database applications.|
|162|11|6|    * [gofight](https://github.com/appleboy/gofight) - API Handler Testing for Golang Router framework.|
|132|6|18|    * [go-mutesting](https://github.com/zimmski/go-mutesting) - Mutation testing for Go source code.|
|130|21|13|    * [ggr](https://github.com/aerokube/ggr) - a lightweight server that routes and proxies Selenium Wedriver requests to multiple Selenium hubs.|
|125|5|0|    * [minimock](https://github.com/gojuno/minimock) - Mock generator for Go interfaces.|
|123|8|11|    * [cdp](https://github.com/mafredri/cdp) - Type-safe bindings for the Chrome Debugging Protocol that can be used with browsers or other debug targets that implement it.|
|109|17|4|    * [GoSpec](https://github.com/orfjackal/gospec) - BDD-style testing framework for the Go programming language.|
|51|6|3|    * [go-txdb](https://github.com/DATA-DOG/go-txdb) - Single transaction based database driver mainly for testing purposes.|
|49|5|1|    * [gospecify](https://github.com/stesla/gospecify) - This provides a BDD syntax for testing your Go code. It should be familiar to anybody who has used libraries such as rspec.|
|45|2|4|    * [restit](https://github.com/yookoala/restit) - Go micro framework to help writing RESTful API integration test.|
|43|0|8|    * [cupaloy](https://github.com/bradleyjkemp/cupaloy) - Simple snapshot testing addon for your test framework.|
|37|5|1|    * [wstest](https://github.com/posener/wstest) - Websocket client for unit-testing a websocket http.Handler.|
|30|4|0|    * [govcr](https://github.com/seborama/govcr) - HTTP mock for Golang: record and replay HTTP interactions for offline testing.|
|29|3|2|    * [dbcleaner](https://github.com/khaiql/dbcleaner) - Clean database for testing purpose, inspired by `database_cleaner` in Ruby.|
|26|6|0|    * [endly](https://github.com/viant/endly) - Declarative end to end functional testing.|
|24|3|1|    * [Hamcrest](https://github.com/rdrdr/hamcrest) - fluent framework for declarative Matcher objects that, when applied to input values, produce self-describing results.|
|20|4|0|    * [bro](https://github.com/marioidival/bro) - Watch files in directory and run tests for them.|
|20|5|0|    * [mockhttp](https://github.com/tv42/mockhttp) - Mock object for Go http.ResponseWriter.|
|15|2|0|    * [dsunit](https://github.com/viant/dsunit) - Datastore testing for SQL, NoSQL, structured files.|
|9|2|0|    * [assert](https://github.com/go-playground/assert) - Basic Assertion Library used along side native go testing, with building blocks for custom assertions.|
|6|1|0|    * [badio](https://github.com/cavaliercoder/badio) - Extensions to Go's `testing/iotest` package.|
|6|2|4|    * [gogiven](https://github.com/corbym/gogiven) - YATSPEC-like BDD testing framework for Go.|
|6|0|0|    * [gocrest](https://github.com/corbym/gocrest) - Composable hamcrest-like matchers for Go assertions.|
|5|0|0|    * [selenoid](https://github.com/aandryashin/selenoid) - alternative Selenium hub server that launches browsers within containers.|
|5|2|1|    * [gosuite](https://github.com/pavlo/gosuite) - Brings lightweight test suites with setup/teardown facilities to `testing` by leveraging Go1.7's Subtests.|
|0|0|0|    * [GoConvey](https://github.com/smartystreets/goconvey/) - BDD-style framework with web UI and live reload.|
## Text Processing

*Libraries for parsing and manipulating texts.*

* Specific Formats
    * [github_flavored_markdown](https://godoc.org/github.com/shurcooL/github_flavored_markdown) - GitHub Flavored Markdown renderer (using blackfriday) with fenced code block highlighting, clickable header anchor links.
* Utility

|stars|forks|issues|description|
| --- | --- | --- | --- |
|5685|506|4|    * [GoQuery](https://github.com/PuerkitoBio/goquery) - GoQuery brings a syntax and a set of features similar to jQuery to the Go language.|
|4397|238|5|    * [colly](https://github.com/asciimoo/colly) - Fast and Elegant Scraping Framework for Gophers|
|3024|388|120|    * [blackfriday](https://github.com/russross/blackfriday) - Markdown processor in Go.|
|2008|250|39|    * [toml](https://github.com/BurntSushi/toml) - TOML configuration format (encoder/decoder with reflection).|
|1449|104|12|    * [go-humanize](https://github.com/dustin/go-humanize) - Formatters for time, numbers, and memory size to human readable format.|
|1071|44|11|    * [sh](https://github.com/mvdan/sh) - Shell parser and formatter.|
|907|61|5|    * [bluemonday](https://github.com/microcosm-cc/bluemonday) - HTML Sanitizer.|
|900|52|5|    * [inject](https://github.com/facebookgo/inject) - Package inject provides a reflect based injector.|
|824|59|18|    * [gofeed](https://github.com/mmcdole/gofeed) - Parse RSS and Atom feeds in Go.|
|486|32|0|    * [commonregex](https://github.com/mingrammer/commonregex) - A collection of common regular expressions for Go|
|344|26|0|    * [xurls](https://github.com/mvdan/xurls) - Extract urls from text.|
|251|56|0|    * [mxj](https://github.com/clbanning/mxj) - Encode / decode XML as JSON or map[string]interface{}; extract values with dot-notation paths and wildcards. Replaces x2j and j2x packages.|
|192|25|0|    * [slug](https://github.com/gosimple/slug) - URL-friendly slugify with multiple languages support.|
|181|31|10|    * [gographviz](https://github.com/awalterschulze/gographviz) - Parses the Graphviz DOT language.|
|167|11|1|    * [gotabulate](https://github.com/bndr/gotabulate) - Easily pretty-print your tabular data with Go.|
|155|14|5|    * [gotext](https://github.com/leonelquinteros/gotext) - GNU gettext utilities for Go.|
|128|21|1|    * [go-runewidth](https://github.com/mattn/go-runewidth) - Functions to get fixed width of the character or string.|
|86|6|1|    * [goq](https://github.com/andrewstuart/goq) - Declarative unmarshaling of HTML using struct tags with jQuery syntax (uses GoQuery).|
|50|1|0|    * [radix](https://github.com/yourbasic/radix) - fast string sorting algorithm.|
|45|4|0|    * [genex](https://github.com/alixaxel/genex) - Count and expand Regular Expressions into all matching Strings.|
|45|13|0|    * [go-nmea](https://github.com/adrianmo/go-nmea) - NMEA parser library for the Go language.|
|38|1|0|    * [align](https://github.com/Guitarbum722/align) - A general purpose application that aligns text.|
|38|2|1|    * [guesslanguage](https://github.com/endeveit/guesslanguage) - Functions to determine the natural language of a unicode text.|
|29|3|2|    * [goregen](https://github.com/zach-klippenstein/goregen) - Library for generating random strings from regular expressions.|
|29|1|0|    * [allot](https://github.com/sbstjn/allot) - Placeholder and wildcard text parsing for CLI tools and bots.|
|25|1|1|    * [gonameparts](https://github.com/polera/gonameparts) - Parses human names into individual name parts.|
|19|6|3|    * [editorconfig-core-go](https://github.com/editorconfig/editorconfig-core-go) - Editorconfig file parser and manipulator for Go.|
|18|2|0|    * [parth](https://github.com/codemodus/parth) - URL path segmentation parsing.|
|17|1|0|    * [Slugify](https://github.com/avelino/slugify) - Go slugify application that handles string.|
|16|3|0|    * [go-slugify](https://github.com/mozillazg/go-slugify) - Make pretty slug with multiple languages support.|
|8|0|0|    * [go-fixedwidth](https://github.com/ianlopshire/go-fixedwidth) - Fixed-width text formatting (encoder/decoder with reflection).|
|8|1|1|    * [xj2go](https://github.com/stackerzzq/xj2go) - Convert xml or json to go struct.|
|7|5|1|    * [go-vcard](https://github.com/emersion/go-vcard) - Parse and format vCard.|
|6|1|0|    * [kace](https://github.com/codemodus/kace) - Common case conversions covering common initialisms.|
|4|2|0|    * [enca](https://github.com/endeveit/enca) - Minimal cgo bindings for [libenca](http://cihar.com/software/enca/).|
|4|0|1|    * [parseargs-go](https://github.com/nproc/parseargs-go) - string argument parser that understands quotes and backslashes.|
|2|0|1|    * [encdec](https://github.com/mickep76/encdec) - Package provides a generic interface to encoders and decodersa.|
|2|1|0|    * [syndfeed](https://github.com/zhengchun/syndfeed) - A syndication feed for Atom 1.0 and RSS 2.0.|
|2|0|0|    * [bbConvert](https://github.com/CalebQ42/bbConvert) - Converts bbCode to HTML that allows you to add support for custom bbCode tags.|
|0|0|0|    * [gommon/bytes](https://github.com/labstack/gommon/tree/master/bytes) - Format bytes to string.|
|0|0|0|    * [doi](https://github.com/hscells/doi) - Document object identifier (doi) parser in Go.|
## Third-party APIs

*Libraries for accessing third party APIs.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3957|917|100|* [aws-sdk-go](https://github.com/aws/aws-sdk-go) - The official AWS SDK for the Go programming language.|
|3550|837|69|* [github](https://github.com/google/go-github) - Go library for accessing the GitHub REST API v3.|
|1584|343|45|* [slack](https://github.com/nlopes/slack) - Slack API in Go.|
|1383|368|48|* [google](https://github.com/google/google-api-go-client) - Auto-generated Google APIs for Go.|
|1073|341|79|* [google-cloud](https://github.com/GoogleCloudPlatform/gcloud-golang) - Google Cloud APIs Go Client Library.|
|1029|174|23|* [telegram-bot-api](https://github.com/Syfaro/telegram-bot-api) - Simple and clean Telegram bot client.|
|882|224|55|* [anaconda](https://github.com/ChimeraCoder/anaconda) - Go client library for the Twitter 1.1 API.|
|687|182|14|* [stripe](https://github.com/stripe/stripe-go) - Go client for the Stripe API.|
|679|240|96|* [goamz](https://github.com/mitchellh/goamz) - Popular fork of [goamz](https://launchpad.net/goamz) which adds some missing API calls to certain packages.|
|630|92|12|* [telebot](https://github.com/tucnak/telebot) - Telegram bot framework written in Go.|
|628|195|2|* [facebook](https://github.com/huandu/facebook) - Go Library that supports the Facebook Graph API.|
|568|134|47|* [discordgo](https://github.com/bwmarrin/discordgo) - Go bindings for the Discord Chat API.|
|469|156|2|* [minio-go](https://github.com/minio/minio-go) - Minio Go Library for Amazon S3 compatible cloud storage.|
|446|88|22|* [go-twitter](https://github.com/dghubble/go-twitter) - Go client library for the Twitter v1.1 APIs.|
|256|115|8|* [go-jira](https://github.com/andygrunwald/go-jira) - Go client library for [Atlassian JIRA](https://www.atlassian.com/software/jira)|
|235|22|2|* [geo-golang](https://github.com/codingsince1985/geo-golang) - Go Library to access [Google Maps](https://developers.google.com/maps/documentation/geocoding/intro), [MapQuest](http://open.mapquestapi.com/geocoding/), [Nominatim](https://developer.mapquest.com/documentation/open/nominatim-search), [OpenCage](http://geocoder.opencagedata.com/api.html), [Bing](https://msdn.microsoft.com/en-us/library/ff701715.aspx), [Mapbox](https://www.mapbox.com/developers/api/geocoding/), and [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Nominatim) geocoding / reverse geocoding APIs.|
|234|5|7|* [githubql](https://github.com/shurcooL/githubql) - Go library for accessing the GitHub GraphQL API v4.|
|218|55|2|* [paypal](https://github.com/logpacker/paypalsdk) - Wrapper for PayPal payment API.|
|175|111|20|* [go-marathon](https://github.com/gambol99/go-marathon) - Go library for interacting with Mesosphere's Marathon PAAS.|
|171|31|2|* [webhooks](https://github.com/go-playground/webhooks) - Webhook receiver for GitHub and Bitbucket.|
|148|20|3|* [tbot](https://github.com/yanzay/tbot) - Telegram bot server with API similar to net/http.|
|108|37|3|* [hipchat (xmpp)](https://github.com/daneharrigan/hipchat) - A golang package to communicate with HipChat over XMPP.|
|107|19|0|* [hipchat](https://github.com/andybons/hipchat) - This project implements a golang client library for the Hipchat API.|
|106|19|4|* [gostorm](https://github.com/jsgilmore/gostorm) - GoStorm is a Go library that implements the communications protocol required to write Storm spouts and Bolts in Go that communicate with the Storm shells.|
|99|14|2|* [Medium](https://github.com/Medium/medium-sdk-go) - Golang SDK for Medium's OAuth2 API.|
|87|8|1|* [go-trending](https://github.com/andygrunwald/go-trending) - Go library for accessing [trending repositories](https://github.com/trending) and [developers](https://github.com/trending/developers) at Github.|
|75|29|5|* [ethrpc](https://github.com/onrik/ethrpc) - Go bindings for Ethereum JSON RPC API.|
|71|2|1|* [go-tgbot](https://github.com/olebedev/go-tgbot) - Pure Golang Telegram Bot API wrapper, generated from swagger file, session-based router and middleware.|
|55|13|8|* [clarifai](https://github.com/samuelcouch/clarifai) - Go client library for interfacing with the Clarifai API.|
|50|10|0|* [megos](https://github.com/andygrunwald/megos) - Client library for accessing an [Apache Mesos](http://mesos.apache.org/) cluster.|
|49|8|0|* [cachet](https://github.com/andygrunwald/cachet) - Go client library for [Cachet (open source status page system)](https://cachethq.io/).|
|48|19|0|* [Trello](https://github.com/adlio/trello) - Go wrapper for the Trello API.|
|46|2|1|* [go-telegraph](https://github.com/toby3d/go-telegraph) - Telegraph publishing platform API client.|
|38|4|0|* [pushover](https://github.com/gregdel/pushover) - Go wrapper for the Pushover API.|
|32|29|5|* [gads](https://github.com/emiddleton/gads) - Google Adwords Unofficial API.|
|31|2|1|* [go-xkcd](https://github.com/nishanths/go-xkcd) - Go client for the xkcd API.|
|31|3|0|* [gcm](https://github.com/Aorioli/gcm) - Go library for Google Cloud Messaging.|
|29|12|5|* [amazon-product-advertising-api](https://github.com/ngs/go-amazon-product-advertising-api) - Go Client Library for [Amazon Product Advertising API](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html).|
|25|10|3|* [GoMusicBrainz](https://github.com/michiwend/gomusicbrainz) - Go MusicBrainz WS2 client library.|
|25|8|1|* [fcm](https://github.com/maddevsio/fcm) - Go library for Firebase Cloud Messaging.|
|24|9|0|* [mixpanel](https://github.com/dukex/mixpanel) - Mixpanel is a library for tracking events and sending Mixpanel profile updates to Mixpanel from your go applications.|
|23|3|0|* [translate](https://github.com/poorny/translate) - Go online translation package.|
|23|20|3|* [circleci](https://github.com/jszwedko/go-circleci) - Go client library for interacting with CircleCI's API.|
|22|15|0|* [gami](https://github.com/bit4bit/gami) - Go library for Asterisk Manager Interface.|
|20|1|0|* [golyrics](https://github.com/mamal72/golyrics) - Golyrics is a Go library to fetch music lyrics data from the Wikia website.|
|18|4|2|* [shopify](https://github.com/rapito/go-shopify) - Go Library to make CRUD request to the Shopify API.|
|16|1|3|* [govkbot](https://github.com/nikepan/govkbot) - Simple Go [VK](https://vk.com) bot library.|
|16|1|0|* [igdb](https://github.com/Henry-Sarabia/igdb) - Go client for the [Internet Game Database API](https://api.igdb.com/).|
|13|1|0|* [go-myanimelist](https://github.com/nstratos/go-myanimelist) - Go client library for accessing the [MyAnimeList API](http://myanimelist.net/modules.php?go=api).|
|13|0|5|* [brewerydb](https://github.com/naegelejd/brewerydb) - Go library for accessing the BreweryDB API.|
|13|1|0|* [spotify](https://github.com/rapito/go-spotify) - Go Library to access Spotify WEB API.|
|12|1|0|* [codeship-go](https://github.com/codeship/codeship-go) - Go client library for interacting with Codeship's API v2.|
|12|3|6|* [go-twitch](https://github.com/knspriggs/go-twitch) - Go client for interacting with the Twitch v3 API.|
|11|0|0|* [patreon-go](https://github.com/mxpv/patreon-go) - Go library for Patreon API.|
|11|0|0|* [textbelt](https://github.com/dietsche/textbelt) - Go client for the textbelt.com txt messaging API.|
|10|1|0|* [TheMovieDb](https://github.com/jbrodriguez/go-tmdb) - Simple golang package to communicate with [themoviedb.org](https://themoviedb.org).|
|8|1|0|* [google-analytics](https://github.com/chonthu/go-google-analytics) - Simple wrapper for easy google analytics reporting.|
|8|0|0|* [smite](https://github.com/sergiotapia/smitego) - Go package to wraps access to the Smite game API.|
|8|3|0|* [steam](https://github.com/sostronk/go-steam) - Go Library to interact with Steam game servers.|
|7|2|6|* [go-unsplash](https://github.com/hbagdi/go-unsplash) - Go client library for the [Unsplash.com](https://unsplash.com) API.|
|6|1|0|* [go-imgur](https://github.com/koffeinsource/go-imgur) - Go client library for [imgur](https://imgur.com)|
|6|2|0|* [micha](https://github.com/onrik/micha) - Go Library for Telegram bot api.|
|5|5|0|* [tumblr](https://github.com/mattcunningham/gumblr) - Go wrapper for the Tumblr v2 API.|
|5|0|0|* [rrdaclient](https://github.com/Omie/rrdaclient) - Go Library to access statdns.com API, which is in turn RRDA API. DNS Queries over HTTP.|
|4|0|0|* [go-sptrans](https://github.com/sergioaugrod/go-sptrans) - Go client library for the SPTrans Olho Vivo API.|
|4|0|0|* [go-hacknews](https://github.com/PaulRosset/go-hacknews) - Tiny Go client for HackerNews API.|
|4|4|0|* [google-email-audit-api](https://github.com/ngs/go-google-email-audit-api) - Go client library for [Google G Suite Email Audit API](https://developers.google.com/admin-sdk/email-audit/).|
|2|3|0|* [zooz](https://github.com/gojuno/go-zooz) - Go client for the Zooz API.|
|1|1|0|* [go-chronos](https://github.com/axelspringer/go-chronos) - Go library for interacting with the [Chronos](https://mesos.github.io/chronos/) Job Scheduler|
|0|0|0|* [playlyfe](https://github.com/playlyfe/playlyfe-go-sdk) - The Playlyfe Rest API Go SDK.|
## Utilities

*General utilities and tools to make your life easier.*

* [clockwerk](http://github.com/onatm/clockwerk) - Go package to schedule periodic jobs using a simple, fluent syntax.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|14401|579|83|* [fzf](https://github.com/junegunn/fzf) - Command-line fuzzy finder written in Go.|
|12786|1266|222|* [hub](https://github.com/github/hub) - wrap git commands with additional functionality to interact with github from the terminal.|
|8186|637|107|* [delve](https://github.com/derekparker/delve) - Go debugger.|
|7378|247|24|* [wuzz](https://github.com/asciimoo/wuzz) - Interactive cli tool for HTTP inspection.|
|6949|238|23|* [ctop](https://github.com/bcicen/ctop) - [Top-like](http://ctop.sh) interface (e.g. htop) for container metrics.|
|4566|148|16|* [peco](https://github.com/peco/peco) - Simplistic interactive filtering tool.|
|4315|371|118|* [sqlx](https://github.com/jmoiron/sqlx) - provides a set of extensions on top of the excellent built-in database/sql package.|
|3541|340|2|* [godropbox](https://github.com/dropbox/godropbox) - Common libraries for writing Go services/applications from Dropbox.|
|2881|144|8|* [go-torch](https://github.com/uber/go-torch) - Stochastic flame graph profiler for Go programs.|
|2835|167|1|* [GJSON](https://github.com/tidwall/gjson) - Get a JSON value with one line of code.|
|2781|144|22|* [goreleaser](https://github.com/goreleaser/goreleaser) - Deliver Go binaries as fast and easily as possible.|
|2386|78|8|* [usql](https://github.com/knq/usql) - usql is a universal command-line interface for SQL databases.|
|2375|455|79|* [xlsx](https://github.com/tealeg/xlsx) - Library to simplify reading the XML format used by recent version of Microsoft Excel in Go programs.|
|2203|101|13|* [realize](https://github.com/tockins/realize) - Go build system with file watchers and live reload. Run, build and watch file changes with custom paths.|
|2039|210|87|* [excelize](https://github.com/360EntSecGroup-Skylar/excelize) - Golang library for reading and writing Microsoft Excel™ (XLSX) files.|
|2021|136|12|* [goreporter](https://github.com/wgliang/goreporter) - Golang tool that does static analysis, unit testing, code review and generate code quality report.|
|1669|227|61|* [gorequest](https://github.com/parnurzeal/gorequest) - Simplified HTTP client with rich features for Go.|
|1667|108|32|* [gojson](https://github.com/ChimeraCoder/gojson) - Automatically generate Go (golang) struct definitions from example JSON.|
|1658|51|6|* [panicparse](https://github.com/maruel/panicparse) - Groups similar goroutines and colorizes stack dump.|
|1426|83|12|* [minify](https://github.com/tdewolff/minify) - Fast minifiers for HTML, CSS, JS, XML, JSON and SVG file formats.|
|1384|34|11|* [mmake](https://github.com/tj/mmake) - Modern Make.|
|1197|46|5|* [coop](https://github.com/rakyll/coop) - Cheat sheet for some of the common concurrent flows in Go.|
|1061|132|30|* [hystrix-go](https://github.com/afex/hystrix-go) - Implements Hystrix patterns of programmer-defined fallbacks aka circuit breaker.|
|1056|53|19|* [grequests](https://github.com/levigross/grequests) - Elegant and simple `net/http` wrapper that follows Python's requests library.|
|958|52|34|* [Storm](https://github.com/asdine/storm) - Simple and powerful toolkit for BoltDB.|
|955|49|3|* [go-underscore](https://github.com/tobyhede/go-underscore) - Useful collection of helpfully functional Go collection utilities.|
|870|99|4|* [resty](https://github.com/go-resty/resty) - Simple HTTP and REST client for Go inspired by Ruby rest-client.|
|861|25|12|* [Task](https://github.com/go-task/task) - simple "Make" alternative.|
|744|45|3|* [profile](https://github.com/pkg/profile) - Simple profiling support package for Go.|
|738|118|13|* [mc](https://github.com/minio/mc) - Minio Client provides minimal tools to work with Amazon S3 compatible cloud storage and filesystems.|
|692|51|36|* [boilr](https://github.com/tmrts/boilr) - Blazingly fast CLI tool for creating projects from boilerplate templates.|
|678|62|11|* [sling](https://github.com/dghubble/sling) - Go HTTP requests builder for API clients.|
|669|94|25|* [goreq](https://github.com/franela/goreq) - Minimal and simple request library for Go language.|
|618|58|14|* [circuitbreaker](https://github.com/rubyist/circuitbreaker) - Circuit Breakers in Go.|
|538|27|29|* [git-time-metric](https://github.com/git-time-metric/gtm) - Simple, seamless, lightweight time tracking for Git.|
|526|21|9|* [gentleman](https://github.com/h2non/gentleman) - Full-featured plugin-driven HTTP client library.|
|511|34|5|* [spinner](https://github.com/briandowns/spinner) - Go package to easily provide a terminal spinner with options.|
|505|19|2|* [gron](https://github.com/roylee0704/gron) - Define time-based tasks using a simple Go API and Gron’s scheduler will run them accordingly.|
|482|17|4|* [immortal](https://github.com/immortal/immortal) - *nix cross-platform (OS agnostic) supervisor.|
|475|27|0|* [httpcontrol](https://github.com/facebookgo/httpcontrol) - Package httpcontrol allows for HTTP transport level control around timeouts and retries.|
|474|96|7|* [mergo](https://github.com/imdario/mergo) - Helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements.|
|449|21|5|* [htcat](https://github.com/htcat/htcat) - Parallel and Pipelined HTTP GET Utility.|
|445|29|1|* [JobRunner](https://github.com/bamzi/jobrunner) - Smart and featureful cron job scheduler with job queuing and live monitoring built in.|
|409|31|5|* [gopencils](https://github.com/bndr/gopencils) - Small and simple package to easily consume REST APIs.|
|401|28|0|* [go-dry](https://github.com/ungerik/go-dry) - DRY (don't repeat yourself) package for Go.|
|386|23|9|* [go-funk](https://github.com/thoas/go-funk) - Modern Go utility library which provides helpers (map, find, contains, filter, chunk, reverse, ...).|
|358|33|5|* [godaemon](https://github.com/VividCortex/godaemon) - Utility to write daemons.|
|292|33|7|* [filetype](https://github.com/h2non/filetype) - Small package to infer the file type checking the magic numbers signature.|
|288|24|5|* [request](https://github.com/mozillazg/request) - Go HTTP Requests for Humans™.|
|255|17|1|* [go-rate](https://github.com/beefsack/go-rate) - Timed rate limiter for Go.|
|248|27|1|* [pester](https://github.com/sethgrid/pester) - Go HTTP client calls with retries, backoff, and concurrency.|
|236|45|0|* [gohper](https://github.com/cosiner/gohper) - Various tools/modules help for development.|
|208|32|5|* [scheduler](https://github.com/carlescere/scheduler) - Cronjobs scheduling made easy.|
|181|27|12|* [ergo](https://github.com/cristianoliveira/ergo) - The management of multiple local services running over different ports made easy.|
|159|9|0|* [go-cron](https://github.com/rk/go-cron) - Simple Cron library for go that can execute closures or functions at varying intervals, from once a second to once a year on a specific date and time. Primarily for web applications and long running daemons.|
|154|5|0|* [go-bind-plugin](https://github.com/wendigo/go-bind-plugin) - go:generate tool for wrapping symbols exported by golang plugins (1.8 only).|
|146|19|1|* [Deepcopier](https://github.com/ulule/deepcopier) - Simple struct copying for Go.|
|144|3|0|* [moldova](https://github.com/StabbyCutyou/moldova) - Utility for generating random data based on an input template.|
|143|8|2|* [rerun](https://github.com/ivpusic/rerun) - Recompiling and rerunning go apps when source changes.|
|134|21|1|* [go-trigger](https://github.com/sadlil/go-trigger) - Go-lang global event triggerer, Register Events with an id and trigger the event from anywhere from your project.|
|126|5|1|* [robustly](https://github.com/VividCortex/robustly) - Runs functions resiliently, catching and restarting panics.|
|110|7|0|* [gojq](https://github.com/elgs/gojq) - JSON query in Golang.|
|106|25|7|* [apm](https://github.com/topfreegames/apm) - Process manager for Golang applications with an HTTP API.|
|92|9|1|* [lrserver](https://github.com/jaschaephraim/lrserver) - LiveReload server for Go.|
|92|12|0|* [Death](https://github.com/vrecan/death) - Managing go application shutdown with signals.|
|88|10|1|* [gotenv](https://github.com/subosito/gotenv) - Load environment variables from `.env` or any `io.Reader` in Go.|
|83|1|0|* [chyle](https://github.com/antham/chyle) - Changelog generator using a git repository with multiple configuration possibilities.|
|78|19|5|* [kazaam](https://github.com/Qntfy/kazaam) - API for arbitrary transformation of JSON documents.|
|78|2|1|* [jsongo](https://github.com/ricardolonga/jsongo) - Fluent API to make it easier to create Json objects.|
|74|4|1|* [onecache](https://github.com/adelowo/onecache) - Caching library with support for multiple backend stores (Redis, Memcached, filesystem etc).|
|71|20|4|* [go-sitemap-generator](https://github.com/ikeikeikeike/go-sitemap-generator) - XML Sitemap generator written in Go.|
|64|22|0|* [goreq](https://github.com/smallnest/goreq) - Enhanced simplified HTTP client based on gorequest.|
|64|3|2|* [UNIS](https://github.com/esemplastic/unis) - Common Architecture™ for String Utilities in Go.|
|61|3|0|* [netbug](https://github.com/e-dard/netbug) - Easy remote profiling of your services.|
|61|9|0|* [util](https://github.com/shomali11/util) - Collection of useful utility functions. (strings, concurrency, manipulations, ...).|
|58|6|2|* [pm](https://github.com/VividCortex/pm) - Process (i.e. goroutine) manager with an HTTP API.|
|54|1|2|* [multitick](https://github.com/VividCortex/multitick) - Multiplexor for aligned tickers.|
|53|2|4|* [xferspdy](https://github.com/monmohan/xferspdy) - Xferspdy provides binary diff and patch library in golang.|
|50|2|2|* [go-health](https://github.com/Talento90/go-health) - Health package simplifies the way you add health check to your services.|
|47|5|0|* [jsonf](https://github.com/miolini/jsonf) - Console tool for highlighted formatting and struct query fetching JSON.|
|45|0|0|* [abutil](https://github.com/bahlo/abutil) - Collection of often-used Golang helpers.|
|44|4|16|* [retry](https://github.com/kamilsk/retry) - Functional mechanism based on context to perform actions repetitively until successful.|
|43|2|0|* [repeat](https://github.com/ssgreg/repeat) - Go implementation of different backoff strategies useful for retrying operations and heartbeating.|
|42|2|0|* [mssqlx](https://github.com/linxGnu/mssqlx) - Database client library, proxy for any master slave, master master structures. Lightweight and auto balancing in mind.|
|37|9|11|* [golog](https://github.com/mlimaloureiro/golog) - Easy and lightweight CLI tool to time track your tasks.|
|36|2|5|* [goback](https://github.com/carlescere/goback) - Go simple exponential backoff package.|
|34|4|0|* [go-astitodo](https://github.com/asticode/go-astitodo) - Parse TODOs in your GO code.|
|34|1|7|* [circuit](https://github.com/cep21/circuit) - An efficient and feature complete Hystrix like Go implementation of the circuit breaker pattern.|
|31|11|1|* [minquery](https://github.com/icza/minquery) - MongoDB / mgo.v2 query that supports efficient pagination (cursors to continue listing documents where we left off).|
|30|2|0|* [golarm](https://github.com/msempere/golarm) - Fire alarms with system events.|
|25|6|1|* [myhttp](https://github.com/inancgumus/myhttp) - Simple API to make HTTP GET requests with timeout support.|
|23|1|1|* [mp](https://github.com/sanbornm/mp) - Simple cli email parser. It currently takes stdin and outputs JSON.|
|23|1|8|* [copy-pasta](https://github.com/jutkko/copy-pasta) - Universal multi-workstation clipboard that uses S3 like backend for the storage.|
|23|4|0|* [toolbox](https://github.com/viant/toolbox) - Slice, map, multimap, struct, function, data conversion utilities. Service router, macro evaluator, tokenizer.|
|21|0|0|* [gpath](https://github.com/tenntenn/gpath) - Library to simplify access struct fields with Go's expression in reflection.|
|21|1|1|* [intrinsic](https://github.com/mengzhuo/intrinsic) - Use x86 SIMD without writing any assembly code.|
|19|2|1|* [retry-go](https://github.com/rafaeljesus/retry-go) - Retrying made simple and easy for golang.|
|19|3|2|* [rclient](https://github.com/zpatrick/rclient) - Readable, flexible, simple-to-use client for REST APIs.|
|18|1|0|* [retry](https://github.com/thedevsaddam/retry) - Simple and easy retry mechanism package for Go.|
|17|4|1|* [goplaceholder](https://github.com/michiwend/goplaceholder) - a small golang lib to generate placeholder images.|
|16|3|0|* [ugo](https://github.com/alxrm/ugo) - ugo is slice toolbox with concise syntax for Go.|
|15|1|1|* [rq](https://github.com/ddo/rq) - A nicer interface for golang stdlib HTTP client.|
|13|0|0|* [dlog](https://github.com/kirillDanshin/dlog) - Compile-time controlled logger to make your release smaller without removing debug calls.|
|12|1|0|* [go-httpheader](https://github.com/mozillazg/go-httpheader) - Go library for encoding structs into Header fields.|
|11|2|0|* [okrun](https://github.com/xta/okrun) - go run error steamroller.|
|10|1|0|* [filler](https://github.com/yaronsumel/filler) - small utility to fill structs using "fill" tag.|
|10|4|1|* [goseaweedfs](https://github.com/linxGnu/goseaweedfs) - SeaweedFS client library with almost full features.|
|9|3|0|* [generate](https://github.com/go-playground/generate) - runs go generate recursively on a specified path or environment variable and can filter by regex.|
|9|2|1|* [rerate](https://github.com/abo/rerate) - Redis-based rate counter and rate limiter for Go.|
|8|1|0|* [go-respond](https://github.com/nicklaw5/go-respond) - Go package for handling common HTTP JSON responses.|
|8|2|0|* [fastlz](https://github.com/digitalcrab/fastlz) - Wrap over [FastLz](http://fastlz.org/) (free, open-source, portable real-time compression library) for GoLang.|
|8|0|0|* [goxlsxwriter](https://github.com/fterrag/goxlsxwriter) - Golang bindings for libxlsxwriter for writing XLSX (Microsoft Excel) files.|
|7|0|0|* [evaluator](https://github.com/nullne/evaluator) - Evaluate an expression dynamicly based on s-expression. It's simple and easy to extend.|
|6|1|0|* [command](https://github.com/txgruppi/command) - Command pattern for Go with thread safe serial and parallel dispatcher.|
|6|2|0|* [jsonhal](https://github.com/RichardKnop/jsonhal) - Simple Go package to make custom structs marshal into HAL compatible JSON responses.|
|5|1|0|* [structs](https://github.com/PumpkinSeed/structs) - Implement simple functions to manipulate structs.|
|4|1|0|* [backscanner](https://github.com/icza/backscanner) - A scanner similar to bufio.Scanner, but it reads and returns lines in reverse order, starting at a given position and going backward.|
|3|1|0|* [jsonapi-errors](https://github.com/AmuzaTkts/jsonapi-errors) - Go bindings based on the JSON API errors reference.|
## Validation

*Libraries for validation.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2595|263|54|* [govalidator](https://github.com/asaskevich/govalidator) - Validators and sanitizers for strings, numerics, slices and structs.|
|1754|133|17|* [validator](https://github.com/go-playground/validator) - Go Struct and Field validation, including Cross Field, Cross Struct, Map, Slice and Array diving.|
|648|36|1|* [ozzo-validation](https://github.com/go-ozzo/ozzo-validation) - Supports validation of various data types (structs, strings, maps, slices, etc.) with configurable and extensible validation rules specified in usual code constructs instead of struct tags.|
|386|25|5|* [govalidator](https://github.com/thedevsaddam/govalidator) - Validate Golang request data with simple rules. Highly inspired by Laravel's request validation.|
|37|8|3|* [validate](https://github.com/markbates/validate) - This package provides a framework for writing validations for Go applications.|
## Version Control

*Libraries for version control.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1145|202|53|* [git2go](https://github.com/libgit2/git2go) - Go bindings for libgit2.|
|62|14|20|* [go-vcs](https://github.com/sourcegraph/go-vcs) - manipulate and inspect VCS repositories in Go.|
|55|7|2|* [gh](https://github.com/rjeczalik/gh) - Scriptable server and net/http middleware for GitHub Webhooks.|
|11|1|0|* [hgo](https://github.com/beyang/hgo) - Hgo is a collection of Go packages providing read-access to local Mercurial repositories.|
## Video

*Libraries for manipulating video.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|460|94|21|* [goav](https://github.com/giorgisio/goav) - Comphrensive Go bindings for FFmpeg.|
|358|81|24|* [gmf](https://github.com/3d0c/gmf) - Go bindings for FFmpeg av\* libraries.|
|204|7|0|* [go-astits](https://github.com/asticode/go-astits) - Parse and demux MPEG Transport Streams (.ts) natively in GO.|
|140|28|10|* [gst](https://github.com/ziutek/gst) - Go bindings for GStreamer.|
|102|5|0|* [go-astisub](https://github.com/asticode/go-astisub) - Manipulate subtitles in GO (.srt, .stl, .ttml, .webvtt, .ssa/.ass, teletext, .smi, etc.).|
|12|2|0|* [v4l](https://github.com/korandiz/v4l) - Video capture library for Linux, written in Go.|
|6|0|0|* [libgosubs](https://github.com/wargarblgarbl/libgosubs) - Subtitle format support for go. Supports .srt, .ttml, and .ass.|
## Web Frameworks

*Full stack web frameworks.*

* [aah](https://aahframework.org) - Scalable, performant, rapid development Web framework for Go.
* [Buffalo](http://gobuffalo.io) - Bringing the productivity of Rails to Go!
* [REST Layer](http://rest-layer.io) - Framework to build REST/GraphQL API on top of databases with mostly configuration over code.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|17173|2017|207|* [Gin](https://github.com/gin-gonic/gin) - Gin is a web framework written in Go! It features a martini-like API with much better performance, up to 40 times faster. If you need performance and good productivity.|
|15246|3321|491|* [Beego](https://github.com/astaxie/beego) - beego is an open-source, high-performance web framework for the Go programming language.|
|10309|899|116|* [Echo](https://github.com/labstack/echo) - High performance, minimalist Go web framework.|
|9808|1240|66|* [Revel](https://github.com/revel/revel) - High-productivity web framework for the Go language.|
|3105|332|42|* [go-json-rest](https://github.com/ant0ine/go-json-rest) - Quick and easy way to setup a RESTful JSON API.|
|2773|275|33|* [goa](https://github.com/raphael/goa) - Framework for developing microservices based on the design of Ruby's Praxis.|
|2342|220|12|* [Macaron](https://github.com/go-macaron/macaron) - Macaron is a high productive and modular design web framework in Go.|
|2202|136|7|* [Gizmo](https://github.com/NYTimes/gizmo) - Microservice toolkit used by the New York Times.|
|2035|135|6|* [utron](https://github.com/gernest/utron) - Lightweight MVC framework for Go(Golang).|
|975|76|28|* [tigertonic](https://github.com/rcrowley/go-tigertonic) - Go framework for building JSON web services inspired by Dropwizard.|
|716|105|9|* [tango](https://github.com/lunny/tango) - Micro & pluggable web framework for Go.|
|514|26|0|* [traffic](https://github.com/pilu/traffic) - Sinatra inspired regexp/pattern mux and web framework for Go.|
|392|13|5|* [gongular](https://github.com/mustafaakin/gongular) - Fast Go web framework with input mapping/validation and (DI) Dependency Injection.|
|361|36|6|* [neo](https://github.com/ivpusic/neo) - Neo is minimal and fast Go Web Framework with extremely simple API.|
|322|36|9|* [mango](https://github.com/paulbellamy/mango) - Mango is a modular web-application framework for Go, inspired by Rack, and PEP333.|
|310|19|8|* [Gondola](https://github.com/rainycape/gondola) - The web framework for writing faster sites, faster.|
|217|17|6|* [Golf](https://github.com/dinever/golf) - Golf is a fast, simple and lightweight micro-web framework for Go. It comes with powerful features and has no dependencies other than the Go Standard Library.|
|153|34|0|* [Gem](https://github.com/go-gem/gem) - Simple and fast web framework, friendly to REST API.|
|147|8|0|* [go-relax](https://github.com/codehack/go-relax) - Framework of pluggable components to build RESTful API's.|
|142|18|0|* [Zerver](https://github.com/cosiner/zerver) - Zerver is an expressive, modular, feature completed RESTful framework.|
|106|10|2|* [go-rest](https://github.com/ungerik/go-rest) - Small and evil REST framework for Go.|
|85|8|0|* [violetear](https://github.com/nbari/violetear) - Go HTTP router.|
|67|5|0|* [Air](https://github.com/sheng/air) - Ideal RESTful web framework for Go.|
|42|2|1|* [YARF](https://github.com/yarf-framework/yarf) - Fast micro-framework designed to build REST APIs and web services in a fast and simple way.|
|41|8|0|* [Microservice](https://github.com/claygod/microservice) - The framework for the creation of microservices, written in Golang.|
|38|11|0|* [Florest](https://github.com/jabong/florest-core) - High-performance workflow based REST API framework.|
|35|4|2|* [WebGo](https://github.com/bnkamalesh/webgo) - A micro-framework to build web apps; with handler chaining, middleware and context injection. With standard library compliant HTTP handlers(i.e. http.HandlerFunc).|
|34|2|0|* [Fireball](https://github.com/zpatrick/fireball) - More "natural" feeling web framework.|
|29|2|0|* [Resoursea](https://github.com/resoursea/api) - REST framework for quickly writing resource based services.|
|17|0|0|* [rex](https://github.com/goanywhere/rex) - Rex is a library for modular development built upon gorilla/mux, fully compatible with `net/http`.|
|1|0|0|* [sawsij](https://github.com/jaybill/sawsij) - lightweight, open-source web framework for building high-performance, data-driven web applications.|
|1|1|1|* [Banjo](https://github.com/nsheremet/banjo) - Very simple and fast web framework for Go.|
### Middlewares

#### Actual middlewares


|stars|forks|issues|description|
| --- | --- | --- | --- |
|856|86|5|* [Tollbooth](https://github.com/didip/tollbooth) - Rate limit HTTP request handler.|
|775|73|2|* [CORS](https://github.com/rs/cors) - Easily add CORS capabilities to your API.|
|689|17|2|* [go-server-timing](https://github.com/mitchellh/go-server-timing) - Add/parse Server-Timing header.|
|329|34|4|* [Limiter](https://github.com/ulule/limiter) - Dead simple rate limit middleware for Go.|
|66|10|1|* [XFF](https://github.com/sebest/xff) - Handle `X-Forwarded-For` header and friends.|
|28|0|0|* [formjson](https://github.com/rs/formjson) - Transparently handle JSON input as a standard form POST.|
|8|0|0|* [client-timing](https://github.com/posener/client-timing) - An HTTP client for Server-Timing header.|
#### Libraries for creating HTTP middlewares


|stars|forks|issues|description|
| --- | --- | --- | --- |
|5526|442|8|* [negroni](https://github.com/urfave/negroni) - Idiomatic HTTP middleware for Golang.|
|1553|99|6|* [alice](https://github.com/justinas/alice) - Painless middleware chaining for Go.|
|1082|89|1|* [render](https://github.com/unrolled/render) - Go package for easily rendering JSON, XML, and HTML template responses.|
|475|35|7|* [stats](https://github.com/thoas/stats) - Go middleware that stores various information about your web application.|
|283|16|1|* [interpose](https://github.com/carbocation/interpose) - Minimalist net/http middleware for golang.|
|203|7|0|* [muxchain](https://github.com/stephens2424/muxchain) - Lightweight middleware for net/http.|
|82|5|0|* [renderer](https://github.com/thedevsaddam/renderer) - Simple, lightweight and faster response (JSON, JSONP, XML, YAML, HTML, File) rendering package for Go.|
|81|1|0|* [Volatile](https://github.com/volatile/core) - Minimalist middleware stack promoting flexibility, good practices and clean code.|
|74|7|1|* [rye](https://github.com/InVisionApp/rye) - Tiny Go middleware library (with canned Middlewares) that supports JWT, CORS, Statsd, and Go 1.7 context.|
|70|1|0|* [gores](https://github.com/alioygur/gores) - Go package that handles HTML, JSON, XML and etc. responses. Useful for RESTful APIs.|
|62|1|0|* [chain](https://github.com/codemodus/chain) - Handler wrapper chaining with scoped data (net/context-based "middleware").|
|52|5|0|* [go-wrap](https://github.com/go-on/wrap) - Small middlewares package for net/http.|
|6|0|0|* [catena](https://github.com/codemodus/catena) - http.Handler wrapper catenation (same API as "chain").|
### Routers


|stars|forks|issues|description|
| --- | --- | --- | --- |
|6960|698|52|* [httprouter](https://github.com/julienschmidt/httprouter) - High performance router. Use this and the standard http handlers to form a very high performance web framework.|
|6083|753|24|* [mux](https://github.com/gorilla/mux) - Powerful URL router and dispatcher for golang.|
|3467|243|17|* [chi](https://github.com/go-chi/chi) - Small, fast and expressive HTTP router built on net/context.|
|1310|101|17|* [gocraft/web](https://github.com/gocraft/web) - Mux and middleware package in Go.|
|1125|102|6|* [pat](https://github.com/bmizerany/pat) - Sinatra style pattern muxer for Go’s net/http library, by the author of Sinatra.|
|1125|78|2|* [Bone](https://github.com/go-zoo/bone) - Lightning Fast HTTP Multiplexer.|
|637|43|3|* [Goji](https://github.com/goji/goji) - Goji is a minimalistic and flexible HTTP request multiplexer with support for `net/context`.|
|479|68|8|* [fasthttprouter](https://github.com/buaazp/fasthttprouter) - High performance router forked from `httprouter`. The first router fit for `fasthttp`.|
|355|18|1|* [lars](https://github.com/go-playground/lars) - Is a lightweight, fast and extensible zero allocation HTTP router for Go used to create customizable frameworks.|
|347|10|0|* [Siesta](https://github.com/VividCortex/siesta) - Composable framework to write middleware and handlers.|
|326|31|1|* [httptreemux](https://github.com/dimfeld/httptreemux) - High-speed, flexible tree-based HTTP router for Go. Inspiration from httprouter.|
|278|43|8|* [ozzo-routing](https://github.com/go-ozzo/ozzo-routing) - An extremely fast Go (golang) HTTP router that supports regular expression route matching. Comes with full support for building RESTful APIs.|
|220|25|13|* [vestigo](https://github.com/husobee/vestigo) - Performant, stand-alone, HTTP compliant URL Router for go web applications.|
|142|9|0|* [gowww/router](https://github.com/gowww/router) - Lightning fast HTTP router fully compatible with the net/http.Handler interface.|
|109|13|2|* [zeus](https://github.com/daryl/zeus) - Very simple and fast HTTP router for Go.|
|101|27|0|* [xujiajun/gorouter](https://github.com/xujiajun/gorouter) - A simple and fast HTTP router for Go.|
|88|6|0|* [alien](https://github.com/gernest/alien) - Lightweight and fast http router from outer space.|
|85|4|0|* [Bxog](https://github.com/claygod/Bxog) - Simple and fast HTTP router for Go. It works with routes of varying difficulty, length and nesting. And he knows how to create a URL from the received parameters.|
|79|7|2|* [xmux](https://github.com/rs/xmux) - High performance muxer based on `httprouter` with `net/context` support.|
|58|3|3|* [pure](https://github.com/go-playground/pure) - Is a lightweight HTTP router that sticks to the std "net/http" implementation.|
|32|3|2|* [GoRouter](https://github.com/vardius/gorouter) - GoRouter is a Server/API micro framwework, HTTP request router, multiplexer, mux that provides request router with middleware supporting `net/context`.|
|17|1|0|* [medeina](https://github.com/imdario/medeina) - Medeina is a HTTP routing tree based on HttpRouter, inspired by Roda and Cuba.|
|13|2|0|* [FastRouter](https://github.com/razonyang/fastrouter) - a fast, flexible HTTP router written in Go.|
## Windows


|stars|forks|issues|description|
| --- | --- | --- | --- |
|383|78|35|* [go-ole](https://github.com/go-ole/go-ole) - Win32 OLE implementation for golang.|
|66|1|0|* [d3d9](https://github.com/gonutz/d3d9) - Go bindings for Direct3D9.|
## XML

*Libraries and tools for manipulating XML.*


# Tools

*Go software and plugins.*

|stars|forks|issues|description|
| --- | --- | --- | --- |
|119|23|0|* [xquery](https://github.com/antchfx/xquery) - XQuery lets you extract data from HTML/XML documents using XPath expression.|
|60|9|1|* [xpath](https://github.com/antchfx/xpath) - XPath package for Go.|
|13|7|8|* [XML-Comp](https://github.com/xml-comp/xml-comp) - Simple command line XML comparer that generates diffs of folders, files and tags.|
|3|0|0|* [xmlwriter](https://github.com/shabbyrobe/xmlwriter) - Procedural XML generation API based on libxml2's xmlwriter module.|
## Code Analysis

* [GoCover.io](http://gocover.io/) - GoCover.io offers the code coverage of any golang package as a service.
* [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports) - Tool to fix (add, remove) your Go imports automatically.
* [GolangCI](https://golangci.com/) - GolangCI is an automated Golang code review service for GitHub pull requests. Service is open source and it's free for open source projects.
* [Golint online](http://go-lint.appspot.com/) - Lints online Go source files on GitHub, Bitbucket and Google Project Hosting using the golint package.
* [goreturns](https://sourcegraph.com/github.com/sqs/goreturns) - Adds zero-value return statements to match the func return types.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|2636|196|35|* [Go Metalinter](https://github.com/alecthomas/gometalinter) - Metalinter is a tool to automatically apply all static analysis tool and report their output in normalized form.|
|2520|317|61|* [GoLint](https://github.com/golang/lint) - Golint is a linter for Go source code.|
|1013|67|17|* [errcheck](https://github.com/kisielk/errcheck) - Errcheck is a program for checking for unchecked errors in Go programs.|
|810|52|9|* [gcvis](https://github.com/davecheney/gcvis) - Visualise Go program GC trace data in real time.|
|699|14|0|* [interfacer](https://github.com/mvdan/interfacer) - Linter that suggests interface types.|
|335|12|5|* [php-parser](https://github.com/z7zmey/php-parser) - A Parser for PHP written in Go.|
|263|20|0|* [goast-viewer](https://github.com/yuroyoro/goast-viewer) - Web based Golang AST visualizer.|
|219|9|1|* [gostatus](https://github.com/shurcooL/gostatus) - Command line tool, shows the status of repositories that contain Go packages.|
|210|10|12|* [unconvert](https://github.com/mdempsky/unconvert) - Remove unnecessary type conversions from Go source.|
|204|16|0|* [go-cleanarch](https://github.com/roblaszczak/go-cleanarch) - go-cleanarch was created to validate Clean Architecture rules, like a The Dependency Rule and interaction between packages in your Go projects.|
|142|2|6|* [apicompat](https://github.com/bradleyfalzon/apicompat) - Checks recent changes to a Go project for backwards incompatible changes.|
|105|5|1|* [dupl](https://github.com/mibk/dupl) - Tool for code clone detection.|
|76|10|4|* [go-checkstyle](https://github.com/qiniu/checkstyle) - checkstyle is a style check tool like java checkstyle. This tool inspired by java checkstyle, golint. The style refered to some points in Go Code Review Comments.|
|62|12|1|* [validate](https://github.com/mccoyst/validate) - Automatically validates struct fields with tags.|
|58|6|0|* [lint](https://github.com/surullabs/lint) - Run linters as part of go test.|
|38|1|0|* [go-outdated](https://github.com/firstrow/go-outdated) - Console application that displays outdated packages.|
|8|1|2|* [tarp](https://github.com/verygoodsoftwarenotvirus/tarp) - tarp finds functions and methods without direct unit tests in Go source code.|
|0|0|0|* [staticcheck](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck) - staticcheck is `go vet` on steroids, applying a ton of static analysis checks you might be used to from tools like ReSharper for C#.|
|0|0|0|* [gosimple](https://github.com/dominikh/go-tools/tree/master/cmd/gosimple) - gosimple is a linter for Go source code that specialises on simplifying code.|
|0|0|0|* [unused](https://github.com/dominikh/go-tools/tree/master/cmd/unused) - unused checks Go code for unused constants, variables, functions and types.|
## Editor Plugins

* [Go plugin for JetBrains IDEs](https://plugins.jetbrains.com/plugin/9568-go) - Go plugin for JetBrains IDEs.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|8461|861|57|* [vim-go](https://github.com/fatih/vim-go) - Go development plugin for Vim.|
|4263|487|63|* [gocode](https://github.com/nsf/gocode) - Autocompletion daemon for the Go programming language.|
|3488|378|162|* [vscode-go](https://github.com/Microsoft/vscode-go) - Extension for Visual Studio Code (VS Code) which provides support for the Go language.|
|2888|261|228|* [GoSublime](https://github.com/DisposaBoy/GoSublime) - Golang plugin collection for the text editor SublimeText 3 providing code completion and other IDE-like features.|
|1378|117|62|* [go-plus](https://github.com/joefitzgerald/go-plus) - Go (Golang) Package For Atom That Adds Autocomplete, Formatting, Syntax Checking, Linting and Vetting.|
|762|134|52|* [go-mode](https://github.com/dominikh/go-mode.el) - Go mode for GNU/Emacs.|
|756|240|47|* [Goclipse](https://github.com/GoClipse/goclipse) - Eclipse plugin for Go.|
|144|21|7|* [Watch](https://github.com/eaburns/Watch) - Runs a command in an acme win on file changes.|
|76|18|0|* [vim-compiler-go](https://github.com/rjohnsondev/vim-compiler-go) - Vim plugin to highlight syntax errors on save.|
|14|3|7|* [velour](https://github.com/velour/velour) - IRC client for the acme editor.|
|10|2|3|* [go-language-server](https://github.com/theia-ide/go-language-server) - A wrapper to turn the VSCode go extension into a language server supporting the language-server-protocol.|
|5|0|3|* [theia-go-extension](https://github.com/theia-ide/theia-go-extension) - Go language support for the Theia IDE.|
## Go Generate Tools

* [gonerics](http://github.com/bouk/gonerics) - Idiomatic Generics in Go.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|1161|69|22|* [gotests](https://github.com/cweill/gotests) - Generate Go tests from your source code.|
|623|44|23|* [genny](https://github.com/cheekybits/genny) - Elegant generics for Go.|
|144|9|4|* [re2dfa](https://github.com/opennota/re2dfa) - Transform regular expressions into finite state machines and output Go source code.|
|15|1|0|* [generic](https://github.com/usk81/generic) - flexible data type for Go.|
## Go Tools

* [gb](https://getgb.io/) - An easy to use project based build tool for the Go programming language.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|2706|198|35|* [OctoLinker](https://github.com/OctoLinker/browser-extension) - Navigate through go files efficiently with the OctoLinker browser extension for GitHub.|
|2241|411|239|* [go-swagger](https://github.com/go-swagger/go-swagger) - Swagger 2.0 implementation for go. Swagger is a simple yet powerful representation of your RESTful API.|
|1111|41|4|* [go-callvis](https://github.com/TrueFurby/go-callvis) - Visualize call graph of your Go program using dot format.|
|263|2|3|* [richgo](https://github.com/kyoh86/richgo) - Enrich `go test` outputs with text decorations.|
|227|8|2|* [depth](https://github.com/KyleBanks/depth) - Visualize dependency trees of any package by analyzing imports.|
|170|7|0|* [rts](https://github.com/galeone/rts) - RTS: response to struct. Generates Go structs from server responses.|
|89|6|1|* [colorgo](https://github.com/songgao/colorgo) - Wrapper around `go` command for colorized `go build` output.|
|35|7|1|* [go-pkg-complete](https://github.com/skelterjohn/go-pkg-complete) - Bash completion for go and wgo.|
|2|0|0|* [generator-go-lang](https://github.com/axelspringer/generator-go-lang) - A [Yeoman](http://yeoman.io) generator to get new Go projects started.|
## Software Packages

*Software written in Go.*

### DevOps Tools

* [Gogs](https://gogs.io/) - A Self Hosted Git Service in the Go Programming Language.
* [Wide](https://wide.b3log.org/login) - Web-based IDE for Teams using Golang.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|48855|14315|3186|* [Moby](https://github.com/moby/moby) - Collaborative project for the container ecosystem to assemble container-based systems.|
|36191|12752|3293|* [kubernetes](https://github.com/kubernetes/kubernetes) - Container Cluster Manager from Google.|
|15112|1498|303|* [traefik](https://github.com/containous/traefik) - Reverse proxy and load balancer with support for multiple backends.|
|7781|486|49|* [Vegeta](https://github.com/tsenart/vegeta) - HTTP load testing tool and library. It's over 9000!|
|7634|2071|352|* [Packer](https://github.com/mitchellh/packer) - Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.|
|6596|694|789|* [Gitea](https://github.com/go-gitea/gitea) - Fork of Gogs, entirely community driven.|
|3522|234|134|* [GVM](https://github.com/moovweb/gvm) - GVM provides an interface to manage Go versions.|
|3266|247|41|* [Hey](https://github.com/rakyll/hey) - Hey is a tiny program that sends some load to a web application.|
|2859|228|35|* [webhook](https://github.com/adnanh/webhook) - Tool which allows user to create HTTP endpoints (hooks) that execute commands on the server.|
|2652|192|36|* [gox](https://github.com/mitchellh/gox) - Dead simple, no frills Go cross compile tool.|
|2527|420|375|* [bosun](https://github.com/bosun-monitor/bosun) - Time Series Alerting Framework.|
|1908|336|50|* [Go Metrics](https://github.com/rcrowley/go-metrics) - Go port of Coda Hale's Metrics library: https://github.com/codahale/metrics.|
|1547|200|155|* [aptly](https://github.com/smira/aptly) - aptly is a Debian repository management tool.|
|1504|68|8|* [goxc](https://github.com/laher/goxc) - build tool for Go, with a focus on cross-compiling and packaging.|
|1200|102|14|* [kala](https://github.com/ajvb/kala) - Simplistic, modern, and performant job scheduler.|
|992|53|3|* [bombardier](https://github.com/codesenberg/bombardier) - Fast cross-platform HTTP benchmarking tool.|
|912|129|41|* [s3gof3r](https://github.com/rlmcpherson/s3gof3r) - Small utility/library optimized for high speed transfer of large objects into and out of Amazon S3.|
|911|94|16|* [Banshee](https://github.com/eleme/banshee) - Anomalies detection system for periodic metrics.|
|910|94|16|* [StatusOK](https://github.com/sanathp/statusok) - Monitor your Website and REST APIs.Get Notified through Slack, E-mail when your server is down or response time is more than expected.|
|582|59|8|* [go-selfupdate](https://github.com/sanbornm/go-selfupdate) - Enable your Go applications to self update.|
|429|59|44|* [Scaleway-cli](https://github.com/scaleway/scaleway-cli) - Manage BareMetal Servers from Command Line (as easily as with Docker).|
|392|26|2|* [skm](https://github.com/TimothyYe/skm) - SKM is a simple and powerful SSH Keys Manager, it helps you to manage your multiple SSH keys easily!|
|293|27|7|* [gonative](https://github.com/inconshreveable/gonative) - Tool which creates a build of Go that can cross compile to all platforms while still using the Cgo-enabled versions of the stdlib packages.|
|281|42|4|* [aurora](https://github.com/xuri/aurora) - Cross-platform web-based Beanstalkd queue server console.|
|247|48|9|* [Mora](https://github.com/emicklei/mora) - REST server for accessing MongoDB documents and meta data.|
|237|10|0|* [govvv](https://github.com/ahmetalpbalkan/govvv) - “go build” wrapper to easily add version information into Go binaries.|
|215|21|7|* [godbg](https://github.com/sirnewton01/godbg) - Web-based gdb front-end application.|
|173|17|6|* [gobrew](https://github.com/cryptojuice/gobrew) - gobrew lets you easily switch between multiple versions of go.|
|173|28|4|* [dogo](https://github.com/liudng/dogo) - Monitoring changes in the source file and automatically compile and run (restart).|
|172|7|15|* [lstags](https://github.com/ivanilves/lstags) - Tool and API to sync Docker images across different registries. |
|159|17|2|* [manssh](https://github.com/xwjdsh/manssh) - manssh is a command line tool for managing your ssh alias config easily.|
|151|13|0|* [ostent](https://github.com/ostrost/ostent) - collects and displays system metrics and optionally relays to Graphite and/or InfluxDB.|
|149|11|0|* [Pewpew](https://github.com/bengadbois/pewpew) - Flexible HTTP command line stress tester.|
|129|2|0|* [Blast](https://github.com/dave/blast) - A simple tool for API load testing and batch jobs.|
|101|4|1|* [grapes](https://github.com/yaronsumel/grapes) - Lightweight tool designed to distribute commands over ssh with ease.|
|43|10|1|* [easyssh-proxy](https://github.com/appleboy/easyssh-proxy) - Golang package for easy remote execution through SSH and SCP downloading via `ProxyCommand`.|
|40|5|10|* [Dropship](https://github.com/chrismckenzie/dropship) - Tool for deploying code via cdn.|
|34|7|0|* [winrm-cli](https://github.com/masterzen/winrm-cli) - Cli tool to remotely execute commands on Windows machines.|
|31|1|6|* [Rodent](https://github.com/alouche/rodent) - Rodent helps you manage Go versions, projects and track dependencies.|
|29|4|4|* [drone-scp](https://github.com/appleboy/drone-scp) - Copy files and artifacts via SSH using a binary, docker or Drone CI.|
|19|1|2|* [kcli](https://github.com/cswank/kcli) - Command line tool for inspecting kafka topics/partitions/messages.|
|13|2|1|* [drone-jenkins](https://github.com/appleboy/drone-jenkins) - Trigger downstream Jenkins jobs using a binary, docker or Drone CI.|
|13|3|0|* [awsenv](https://github.com/soniah/awsenv) - Small binary that loads Amazon (AWS) environment variables for a profile.|
|2|0|2|* [sg](https://github.com/ChristopherRabotin/sg) - Benchmarks a set of HTTP endpoints (like ab), with possibility to use the reponse code and data between each call for specific server stress based on its previous response.|
### Other Software
* [Docker](http://www.docker.com/) - Open platform for distributed applications for developers and sysadmins.
* [GoLand](https://jetbrains.com/go) - Full featured cross-platform Go IDE.
* [hugo](http://gohugo.io/) - Fast and Modern Static Website Engine.
* [Juju](https://jujucharms.com/) - Cloud-agnostic service deployment and orchestration - supports EC2, Azure, Openstack, MAAS and more.
* [limetext](http://limetext.org/) - Lime Text is a powerful and elegant text editor primarily developed in Go that aims to be a Free and open-source software successor to Sublime Text.
* [syncthing](https://syncthing.net/) - Open, decentralized file synchronization tool and protocol.
* [tsuru](https://tsuru.io/) - Extensible and open source Platform as a Service software.

# Resources

*Where to discover new Go libraries.*

|stars|forks|issues|description|
| --- | --- | --- | --- |
|8835|826|104|* [Gor](https://github.com/buger/gor) - Http traffic replication tool, for replaying traffic from production to stage/dev environments in real-time.|
|7953|762|461|* [rkt](https://github.com/coreos/rkt) - App Container runtime that integrates with init systems, is compatible with other container formats like Docker, and supports alternative execution engines like KVM.|
|5465|221|16|* [Comcast](https://github.com/tylertreat/Comcast) - Simulate bad network connections.|
|5339|723|49|* [Seaweed File System](https://github.com/chrislusf/seaweedfs) - Fast, Simple and Scalable Distributed File System with O(1) disk seek.|
|5000|850|58|* [confd](https://github.com/kelseyhightower/confd) - Manage local application configuration files using templates and data from etcd or consul.|
|4437|596|270|* [LiteIDE](https://github.com/visualfc/liteide) - LiteIDE is a simple, open source, cross-platform Go IDE.|
|4284|323|222|* [restic](https://github.com/restic/restic) - De-duplicating backup program.|
|3568|282|5|* [nes](https://github.com/fogleman/nes) - Nintendo Entertainment System (NES) emulator written in Go.|
|2723|151|34|* [toxiproxy](https://github.com/shopify/toxiproxy) - Proxy to simulate network and system conditions for automated tests.|
|2415|307|106|* [fleet](https://github.com/coreos/fleet) - Distributed init System.|
|2026|165|13|* [myLG](https://github.com/mehrdadrad/mylg) - Command Line Network Diagnostic tool written in Go.|
|1719|257|141|* [snap](https://github.com/intelsdi-x/snap) - Powerful telemetry framework.|
|1712|75|30|* [Stack Up](https://github.com/pressly/sup) - Stack Up, a super simple deployment tool - just Unix - think of it like 'make' for a network of servers.|
|1638|137|8|* [Circuit](https://github.com/gocircuit/circuit) - Circuit is a programmable platform-as-a-service (PaaS) and/or Infrastructure-as-a-Service (IaaS), for management, discovery, synchronization and orchestration of services and hosts comprising cloud applications.|
|1321|40|11|* [borg](https://github.com/crufter/borg) - Terminal based search engine for bash snippets.|
|894|142|4|* [Pipe](https://github.com/b3log/pipe) - A small and beautiful blogging platform.|
|846|28|11|* [Go Package Store](https://github.com/shurcooL/Go-Package-Store) - App that displays updates for the Go packages in your GOPATH.|
|710|48|8|* [Postman](https://github.com/zachlatta/postman) - Command-line utility for batch-sending email.|
|571|39|12|* [Leaps](https://github.com/jeffail/leaps) - Pair programming service using Operational Transforms.|
|487|62|19|* [peg](https://github.com/pointlander/peg) - Peg, Parsing Expression Grammar, is an implementation of a Packrat parser generator.|
|416|44|12|* [Documize](https://github.com/documize/community) - Modern wiki software that integrates data from SaaS tools.|
|375|72|10|* [vFlow](https://github.com/VerizonDigital/vflow) - High-performance, scalable and reliable IPFIX, sFlow and Netflow collector.|
|356|38|2|* [mockingjay](https://github.com/quii/mockingjay-server) - Fake HTTP servers and consumer driven contracts from one configuration file. You can also make the server randomly misbehave to help do more realistic performance tests.|
|267|16|23|* [wellington](https://github.com/wellington/wellington) - Sass project management tool, extends the language with sprite functions (like Compass).|
|225|28|2|* [shell2http](https://github.com/msoap/shell2http) - Executing shell commands via http server (for prototyping or remote control).|
|221|28|7|* [ipe](https://github.com/dimiro1/ipe) - Open source Pusher server implementation compatible with Pusher client libraries written in GO.|
|204|38|1|* [GoDNS](https://github.com/timothyye/godns) - A dynamic DNS client tool, supports DNSPod & HE.net, written in Go.|
|172|8|0|* [ide](https://github.com/thestrukture/ide) - Browser accessible IDE. Designed for Go with Go.|
|170|14|19|* [gocc](https://github.com/goccmack/gocc) - Gocc is a compiler kit for Go written in Go.|
|162|6|1|* [orange-cat](https://github.com/noraesae/orange-cat) - Markdown previewer written in Go.|
|162|15|13|* [Tenyks](https://github.com/kyleterry/tenyks) - Service oriented IRC bot using Redis and JSON for messaging.|
|158|22|0|* [Cherry](https://github.com/rafael-santiago/cherry) - Tiny webchat server in Go.|
|88|4|0|* [Orbit](https://github.com/gulien/orbit) - A simple tool for running commands and generating files from templates.|
|67|7|0|* [boxed](https://github.com/tejo/boxed) - Dropbox based blog engine.|
|44|4|1|* [DDNS](https://github.com/skibish/ddns) - Personal DDNS client with Digital Ocean Networking DNS as backend.|
|42|8|6|* [websysd](https://github.com/ian-kent/websysd) - Web based process manager (like Marathon or Upstart).|
|20|4|0|* [toto](https://github.com/blogcin/ToTo) - Simple proxy server written in Go language, can be used together with browser.|
|14|1|5|* [Snitch](https://github.com/lucasgomide/snitch) - Simple way to notify your team and many tools when someone has deployed any application via Tsuru.|
|11|0|0|* [GoDocTooltip](https://github.com/diankong/GoDocTooltip) - Chrome extension for Go Doc sites, which shows function description as tooltip at funciton list.|
|11|1|0|* [JayDiff](https://github.com/yazgazan/jaydiff) - JSON diff utility written in Go.|
|10|0|0|* [naclpipe](https://github.com/unix4fun/naclpipe) - Simple NaCL EC25519 based crypto pipe tool written in Go.|
|10|2|0|* [term-quiz](https://github.com/crazcalm/term-quiz) - Quizzes for your terminal.|
## Benchmarks


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1065|135|25|* [go-http-routing-benchmark](https://github.com/julienschmidt/go-http-routing-benchmark) - Go HTTP request router benchmark and comparison.|
|843|125|31|* [skynet](https://github.com/atemerev/skynet) - Skynet 1M threads microbenchmark.|
|708|87|3|* [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) - Go web framework benchmark.|
|642|63|4|* [go_serialization_benchmarks](https://github.com/alecthomas/go_serialization_benchmarks) - Benchmarks of Go serialization methods.|
|131|14|0|* [speedtest-resize](https://github.com/fawick/speedtest-resize) - Compare various Image resize algorithms for the Go language.|
|96|12|0|* [go-benchmarks](https://github.com/tylertreat/go-benchmarks) - Few miscellaneous Go microbenchmarks. Compare some language features to alternative approaches.|
|87|23|2|* [autobench](https://github.com/davecheney/autobench) - Framework to compare the performance between different Go versions.|
|80|6|1|* [gospeed](https://github.com/feyeleanor/GoSpeed) - Go micro-benchmarks for calculating the speed of language constructs.|
|50|2|0|* [gocostmodel](https://github.com/PuerkitoBio/gocostmodel) - Benchmarks of common basic operations for the Go language.|
|43|6|2|* [golang-sql-benchmark](https://github.com/tyler-smith/golang-sql-benchmark) - Collection of benchmarks for popular Go database/SQL utilities.|
|14|0|0|* [golang-micro-benchmarks](https://github.com/amscanne/golang-micro-benchmarks) - Tiny collection of Go micro benchmarks. The intent is to compare some language features to others.|
|13|2|0|* [go-benchmark-app](https://github.com/mrLSD/go-benchmark-app) - Powerful HTTP-benchmark tool mixed with Аb, Wrk, Siege tools. Gathering statistics and various parameters for benchmarks and comparison results.|
|12|1|0|* [kvbench](https://github.com/jimrobinson/kvbench) - Key/Value database benchmark.|
|4|1|1|* [go-type-assertion-benchmark](https://github.com/hgfischer/go-type-assertion-benchmark) - Naive performance test of two ways to do type assertion in Go.|
## Conferences

* [Capital Go](http://www.capitalgolang.com) - Washington, D.C., USA
* [dotGo](http://www.dotgo.eu) - Paris, France
* [GoCon](http://gocon.connpass.com/) - Tokyo, Japan
* [GoLab](http://golab.io/) - Florence, Italy
* [GolangUK](http://golanguk.com/) - London, UK
* [GopherChina](http://gopherchina.org) - Shanghai, China
* [GopherCon](http://www.gophercon.com/) - Denver, USA
* [GopherCon Brazil](https://gopherconbr.org) - Florianópolis, BR
* [GopherCon Europe](https://gophercon.is/) - Reykjavik, Iceland
* [GopherCon Russia](https://www.gophercon-russia.ru) - Moscow, Russia
* [GopherCon Singapore](https://gophercon.sg) - Mapletree Business City, Singapore
* [GothamGo](http://gothamgo.com/) - New York City, USA

## E-Books

* [A Go Developer's Notebook](https://leanpub.com/GoNotebook/read)
* [An Introduction to Programming in Go](http://www.golang-book.com/)
* [Build Web Application with Golang](https://www.gitbook.com/book/astaxie/build-web-application-with-golang/details)
* [Building Web Apps With Go](https://www.gitbook.com/book/codegangsta/building-web-apps-with-go/details)
* [Go 101](https://go101.org) - A book focusing on Go syntax/semantics and all kinds of details
* [Go Bootcamp](http://golangbootcamp.com)
* [Learning Go](https://www.miek.nl/downloads/Go/Learning-Go-latest.pdf)
* [Network Programming With Go](https://jan.newmarch.name/go/)
* [The Go Programming Language](http://www.gopl.io/)
* [Web Application with Go the Anti-Textbook](https://github.com/thewhitetulip/web-dev-golang-anti-textbook/)

|stars|forks|issues|description|
| --- | --- | --- | --- |
|4859|620|10|* [GoBooks](https://github.com/dariubs/GoBooks) - A curated list of Go books.|
## Gophers

* [gopher-stickers](https://github.com/tenntenn/gopher-stickers)
* [gopher-vector](https://github.com/golang-samples/gopher-vector)
* [gophericons](https://github.com/shalakhin/gophericons)

|stars|forks|issues|description|
| --- | --- | --- | --- |
|1246|46|8|* [gophers](https://github.com/ashleymcnamara/gophers) - Gopher artworks by Ashley McNamara|
|1058|34|1|* [gophers](https://github.com/egonelbre/gophers) - Free gophers|
|200|21|7|* [gopherize.me](https://github.com/matryer/gopherize.me) - Gopherize yourself|
|44|1|2|* [gophers](https://github.com/rogeralsing/gophers) - random gopher graphics|
|34|1|0|* [gopher-logos](https://github.com/GolangUA/gopher-logos) - adorable gopher logos|
|20|2|0|* [Go-gopher-Vector](https://github.com/keygx/Go-gopher-Vector) - Go gopher Vector Data [.ai, .svg]|
|14|0|0|* [gophers](https://github.com/sillecelik/go-gopher) - Gopher amigurumi toy pattern|
## Meetups

* [Go Language NYC](https://www.meetup.com/golanguagenewyork/)
* [Go London User Group](https://www.meetup.com/Go-London-User-Group/)
* [Go Toronto](https://www.meetup.com/go-toronto/)
* [Go User Group Atlanta](https://www.meetup.com/Go-Users-Group-Atlanta/)
* [GoBridge, San Francisco, CA](https://www.meetup.com/gobridge/)
* [GoJakarta](https://www.meetup.com/GoJakarta/)
* [Golang Amsterdam](https://www.meetup.com/golang-amsterdam/)
* [Golang Argentina](https://www.meetup.com/Golang-Argentina/)
* [Golang Bangalore](https://www.meetup.com/Golang-Bangalore/)
* [Golang Belo Horizonte - Brazil](https://www.meetup.com/go-belo-horizonte/)
* [Golang Boston](https://www.meetup.com/bostongo/)
* [Golang Bulgaria](https://www.meetup.com/Golang-Bulgaria/)
* [Golang Cardiff, UK](https://www.meetup.com/Cardiff-Go-Meetup/)
* [Golang Copenhagen](https://www.meetup.com/Go-Cph/)
* [Golang DC, Arlington, VA](https://www.meetup.com/Golang-DC/)
* [Golang Dorset, UK](https://www.meetup.com/golang-dorset/)
* [Golang Israel](https://www.meetup.com/Go-Israel/)
* [Golang Joinville - Brazil](https://www.meetup.com/Joinville-Go-Meetup/)
* [Golang Lima - Peru](https://www.meetup.com/Golang-Peru/)
* [Golang Lyon](https://www.meetup.com/Golang-Lyon/)
* [Golang Melbourne](https://www.meetup.com/golang-mel/)
* [Golang Mountain View](https://www.meetup.com/Golang-Mountain-View/)
* [Golang New York](https://www.meetup.com/nycgolang/)
* [Golang Paris](https://www.meetup.com/Golang-Paris/)
* [Golang Pune](https://www.meetup.com/Golang-Pune/)
* [Golang Singapore](https://www.meetup.com/golangsg/)
* [Golang Stockholm](https://www.meetup.com/Go-Stockholm/)
* [Golang Syney, AU](https://www.meetup.com/golang-syd/)
* [Golang São Paulo - Brazil](https://www.meetup.com/golangbr/)
* [Golang Vancouver, BC](https://www.meetup.com/golangvan/)
* [Golang Москва](https://www.meetup.com/Golang-Moscow/)
* [Golang Питер](https://www.meetup.com/Golang-Peter/)
* [Istanbul Golang](https://www.meetup.com/Istanbul-Golang/)
* [Seattle Go Programmers](https://www.meetup.com/golang/)
* [Ukrainian Golang User Groups](https://www.meetup.com/uagolang/)
* [Utah Go User Group](https://www.meetup.com/utahgophers/)
* [Women Who Go - San Francisco, CA](https://www.meetup.com/Women-Who-Go/)

*Add the group of your city/country here (send **PR**)*

## Twitter

* [@golang](https://twitter.com/golang)
* [@golang_news](https://twitter.com/golang_news)
* [@golangflow](https://twitter.com/golangflow)
* [@golangweekly](https://twitter.com/golangweekly)

## Websites

* [Awesome Go @LibHunt](https://go.libhunt.com) - Your go-to Go Toolbox.
* [Go Blog](http://blog.golang.org) - The official Go blog.
* [Go Challenge](http://golang-challenge.org/) - Learn Go by solving problems and getting feedback from Go experts.
* [Go Forum](https://forum.golangbridge.org) - Forum to discuss Go.
* [Go In 5 Minutes](https://www.goin5minutes.com/) - 5 minute screencasts focused on getting one thing done.
* [Go Report Card](https://goreportcard.com) - A report card for your Go package.
* [godoc.org](https://godoc.org/) - Documentation for open source Go packages.
* [Golang Flow](https://golangflow.io) - Post Updates, News, Packages and more.
* [Golang News](https://golangnews.com) - Links and news about Go programming.
* [golang-nuts](https://groups.google.com/forum/#!forum/golang-nuts) - Go mailing list.
* [Google Plus Community](https://plus.google.com/communities/114112804251407510571) - The Google+ community for #golang enthusiasts.
* [Gopher Community Chat](https://invite.slack.golangbridge.org) - Join Our New Slack Community For Gophers ([Understand how it came](https://blog.gopheracademy.com/gophers-slack-community/)).
* [gowalker.org](https://gowalker.org) - Go Project API documentation.
* [justforfunc](https://www.youtube.com/c/justforfunc) - Youtube channel dedicated to Go programming language tips and tricks, hosted by  Francesc Campoy [@francesc](https://twitter.com/francesc).
* [r/Golang](https://www.reddit.com/r/golang) - News about Go.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|21402|2766|3|* [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) - List of other amazingly awesome lists.|
|11716|1147|6|* [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job) - Curated list of awesome remote jobs. A lot of them are looking for Go hackers.|
|132|8|1|* [golang-graphics](https://github.com/mholt/golang-graphics) - Collection of Go images, graphics, and art.|
|28|0|0|* [gocryforhelp](https://github.com/ninedraft/gocryforhelp) - Collection of Go projects that needs help. Good place to start your open-source way in Go.|
|0|0|0|* [Trending Go repositories on GitHub today](https://github.com/trending?l=go) - Good place to find new Go libraries.|
|0|0|0|* [Go Projects](https://github.com/golang/go/wiki/Projects) - List of projects on the Go community wiki.|
### Tutorials

* [A Tour of Go](http://tour.golang.org/) - Interactive tour of Go.
* [Building Go Web Applications and Microservices Using Gin](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin) - Get familiar with Gin and find out how it can help you reduce boilerplate code and build a request handling pipeline.
* [Games With Go](http://gameswithgo.org/) - A video series teaching programming and game development.
* [Go By Example](https://gobyexample.com/) - Hands-on introduction to Go using annotated example programs.
* [Go database/sql tutorial](http://go-database-sql.org/) - Introduction to database/sql.
* [Golangbot](https://golangbot.com/learn-golang-series/) - Tutorials to get started with programming in Go.
* [Hackr.io](https://hackr.io/tutorials/learn-golang) - Learn Go from the best online golang tutorials submitted & voted by the golang programming community.
* [How to Use Godog for Behavior-driven Development in Go](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go) - Get started with Godog — a Behavior-driven development framework for building and testing Go applications.
* [Your basic Go](http://yourbasic.org/golang) - Huge collection of tutorials and how to's
