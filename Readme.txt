local OrionLib = loadstring(game:HttpGet(('https://raw.githubusercontent.com/shlexware/Orion/main/source')))()
local fakeValues = {
    WalkSpeed = 16,
    JumpPower = 50
}
local enabledProperties = {
    WalkSpeed = false,
    JumpPower = false
}
local oldIndex

oldIndex = hookmetamethod(game, "__index", function(self, key)
    if tostring(self) == "Humanoid" and enabledProperties[key] then
        if fakeValues[key] then
            return fakeValues[key]
        end
    end
    return oldIndex(self, key)
end)

OrionLib:MakeNotification({
    Name = "Disclaimer",
    Content = "Works only if anti-cheat checks WalkSpeed/JumpPower values.",
    Image = "rbxassetid://45tv483345998",
    Time = 3
})

task.wait(3)

OrionLib:MakeNotification({
    Name = "Important Note",
    Content = "Won't work if anti-cheat monitors hook functions.",
    Image = "rbxassetid://4483345998",
    Time = 3
})

task.wait(3)

OrionLib:MakeNotification({
    Name = "Limitations",
    Content = "Client-side only; doesn't affect the server.",
    Image = "rbxassetid://4483345998",
    Time = 3
})

task.wait(3)

OrionLib:MakeNotification({
    Name = "Test Environment",
    Content = "Go to the game: https://www.roblox.com/games/130999049368928/SecureRemoteEvent",
    Image = "rbxassetid://4483345998",
    Time = 3
})

task.wait(3)

if game.PlaceId == 130999049368928 then
    OrionLib:MakeNotification({
        Name = "Test Instructions",
        Content = "You are in the test game. Touch the green part to set your speed to 100. Use the hub to fake it. If faked, you won't be kicked.",
        Image = "rbxassetid://4483345998",
        Time = 9
    })
end

task.wait(10)

local Window = OrionLib:MakeWindow({Name = "Fake Property Control", HidePremium = false, SaveConfig = true, ConfigFolder = "OrionConfig"})

local MainTab = Window:MakeTab({
    Name = "Main",
    Icon = "rbxassetid://4483345998",
    PremiumOnly = false
})

MainTab:AddLabel("This is the beginning of the hub. I'm gonna add more stuff!")

MainTab:AddToggle({
    Name = "Enable Fake WalkSpeed",
    Default = false,
    Callback = function(value)
        enabledProperties.WalkSpeed = value
        print("Fake WalkSpeed toggled:", value)
    end
})

MainTab:AddTextbox({
    Name = "Set Fake WalkSpeed",
    Default = tostring(fakeValues.WalkSpeed),
    TextDisappear = false,
    Callback = function(value)
        local num = tonumber(value)
        if num then
            fakeValues.WalkSpeed = num
            print("Fake WalkSpeed set to:", num)
        else
            print("Invalid input for WalkSpeed")
        end
    end
})

MainTab:AddToggle({
    Name = "Enable Fake JumpPower",
    Default = false,
    Callback = function(value)
        enabledProperties.JumpPower = value
        print("Fake JumpPower toggled:", value)
    end
})

MainTab:AddTextbox({
    Name = "Set Fake JumpPower",
    Default = tostring(fakeValues.JumpPower),
    TextDisappear = false,
    Callback = function(value)
        local num = tonumber(value)
        if num then
            fakeValues.JumpPower = num
            print("Fake JumpPower set to:", num)
        else
            print("Invalid input for JumpPower")
        end
    end
})

OrionLib:Init()
