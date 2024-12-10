require 'rubygems'
require 'mqtt'
require 'readline'
nickname=ARGV[0]
mqtt=MQTT::client,new('localhost')
mqtt.connect do[client0]
    client.subscribe('chat/public')
    client.subscribe("chat/private/#(nickname)")
    enter_msg="#(nickname) enter room!!"
    client.publish 'chat/public',enter_msg
    Thread.new do
        while message=readline,readline("",true)
            case message
                when/^\/priv\s*(\w*)\s*(.*)/
                    client.publish "chat/private/#{$1}", "<#{nickname}>:#{$2}"
                when /^\?quit\s*(.*)/
                    client.publish 'chat/public',"#{nickname}has quit (#{$1})"
                    exit 1
                else
                    client.publish 'chat/public',"#{nickname} :#{message}"
                end
            end
        end
        loop do 
            topic,message=client.get
            print message,"\n"
        end
    end