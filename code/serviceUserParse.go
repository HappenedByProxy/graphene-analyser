// This file handles the "user" service.
package main

import (
	"fmt"
	"strings"
)

// Setting represents a setting with its attributes
type Setting struct {
	Flags                   string // The flags the user profile has.
	State                   string // Is it running? Is it locked? Is it the current profile?
	Created                 string // When was the profile created?
	LastLoggedIn            string // When did someone last log into the profile?
	LastLoggedFingerprint   string // Who logged in?
	StartTime 				string  // When was it started?
	UnlockTime 				string // When did we first unlock?
	IsOwner 				string // Is this the owner profile?
}

// The date timestamps are in this format:  Last logged in: +17d2h32m27s216ms ago
// We need to break it down. 


// This function, which will be renamed later, can be recycled for 'created, last logged in, start time, unlock time and last entered foreground'.
func main() {

	// Test snip. We need to code it so it only works on the appropriate lines, being "Created" and "Last logged in".
    absoluteUnit := `
    user
    UserInfo{10:Google:410} serialNo=21 isPrimary=false
    Type: android.os.usertype.full.SECONDARY
    Flags: 1040 (FULL|INITIALIZED)
    State: RUNNING_UNLOCKED
    Created: +796d8h22m39s820ms ago
    Last logged in: +17d2h32m27s216ms ago
    `

	// We need to break down the data into individual lines. The strings split maybe?

	// Then we need to check that the lines we are using only has "Created:" or whatever else.
	// Read: https://pkg.go.dev/strings#HasPrefix
	// if strings.HasPrefix("Created:") || strings.HasPrefix("Last logged in:") then {
		// The other process that is below? Maybe just put it into a func? 
	// }
	
	// If we want to keep that variable, we need to use it. Else the code does not run.
	fmt.Println(absoluteUnit)
// Later, we need to be feeding this from a full user log file.
testString := "Last logged in: +17d2h32m27s216ms ago"

// Get the index of +.
plusIndex := strings.Index(testString, "+")
if plusIndex != -1 {
	// This gives us +17d2h32m27s216ms ago
	testString = testString[plusIndex:]
}

// Now lets remove the "ago" by understanding where "ago" is.
agoIndex := strings.Index(testString, " ago")
if agoIndex != -1 {
	testString = testString[:agoIndex]
}

// This SHOULD give us just the timestamp, like +17d2h32m27s216ms
fmt.Println(testString)

// Now we need to break down this string. Somehow.

// Something like:
// 17d
// 2h
// 32m
// 27s
// 216ms

// Then make that into
// 17 days
// 2 hours
// 32 minutes
// 27 seconds
// 216 milliseconds
// ago.

// Alternatively..
// Get the current date, and then somehow try to... provide a date? If the date is 25/06/2024, then take away 17 days?

}