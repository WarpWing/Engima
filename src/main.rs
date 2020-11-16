extern crate clap;
use clap::App; 

fn main() { 
    App::new("mps")
       .version("v1.0")
       .about("A Rust Written TUI designed to help users navitage Canonical's Multipass VM System with ease.")
       .author("Ty Chermsirivatana")
       .get_matches(); 
}