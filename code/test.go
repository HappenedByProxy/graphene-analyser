// THIS CODE IS AI GENERATED.
// FROM A CHAT I DON'T HAVE ANYMORE.

package main

import (
	"fmt"
	"strings"
)

// Setting represents a setting with its attributes
type Setting struct {
	ID               string // It's always going to have an ID, and the ID isn't going to be letters. But to save unnecessary conversion from int to string later, just put it as a string.
	Name             string // Name of the setting we are parsing.
	Pkg              string // The package the setting belongs to. Will likely be android or com.settings.android, but this may change.
	Value            string // 0 = false, 1 = true
	Default          string // The default value for this setting. 0 = false, 1 = true
	DefaultSystemSet string // Whether this was set by the system. Is this a dupe of Default? 0 = false, 1 = true
}


// parseSetting takes a string and parses it into a Setting struct
func parseSetting(input string) Setting {
	// Split the string by spaces
	parts := strings.Fields(input)

	// Create a map to hold the parsed key-value pairs
	data := make(map[string]string)

	// Iterate over the parts and split by colon to get key-value pairs
	for _, part := range parts {
		kv := strings.Split(part, ":")
		if len(kv) == 2 {
			data[kv[0]] = kv[1]
		}
	}

	// Create a Setting struct and populate it with the parsed values
	setting := Setting{
		ID:               data["_id"],
		Name:             data["name"],
		Pkg:              data["pkg"],
		Value:            data["value"],
		Default:          data["default"],
		DefaultSystemSet: data["defaultSystemSet"],
	}

	return setting
}

func main() {
	// Example input string
	inputs := []string{
		"_id:402 name:adb_wifi_enabled pkg:android value:0 default:0 defaultSystemSet:true",
		"_id:15 name:cell_on pkg:android value:1 default:1 defaultSystemSet:true",
	}



	// Print the parsed values
	for _, input := range inputs {
	// Parse the input string into a Setting struct
		setting := parseSetting(input)
		fmt.Printf("ID: %s\n", setting.ID)
		fmt.Printf("Name: %s\n", setting.Name)
		fmt.Printf("Pkg: %s\n", setting.Pkg)
		fmt.Printf("Value: %s\n", setting.Value)
		fmt.Printf("Default: %s\n", setting.Default)
		fmt.Printf("DefaultSystemSet: %s\n", setting.DefaultSystemSet)

		// Example of combining name and status into "<name>:<status>"
		fmt.Printf("%s:%s\n", setting.Name, setting.Value)
		fmt.Printf("\n")
	}
}

