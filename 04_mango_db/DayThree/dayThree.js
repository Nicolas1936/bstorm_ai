

var db = db.getSiblingDB('DayThree');

db.editors.drop()
db.authors.drop()
db.books.drop()

var validColl = db.editors.validate();

//printjson(validColl);
if(!validColl.valid)
{
    db.createCollection("editors", 
    {
        validator: 
        {
            $jsonSchema: 
            {
                bsonType: "object",
                required: [ "NbrTVA", "name" ],
                properties: 
                {
                    NbrTVA: {
                        bsonType: "string",
                        description: ""
                    },
                    name:
                    {
                        bsonType: "string",
                        description: ""
                    },
                    creationDate:
                    {
                        bsonType: "date",
                        description: ""
                    },
                    books:
                    {
                        bsonType: "array",
                        items: 
                        {
                            bsonType: "objectId",
                            description: ""
                        }
                    }
                }
            }
        }
    });

    db.editors.createIndex({ "NbrTVA": 1 }, { unique: true });
    db.editors.createIndex({ "name": 1 }, { unique: true });

    print("Collection 'editors' a été créé!")

} else {
    print("Collection 'editors' existe déjà!" )
}

//-------------------------------------------------------------------

//books : 
//- required : isbn, title, authors, editor
//- properties : isbn : string , title : string, authors [ObjectID], editor objectID, releaseDate date
//- index : isbn : unique

var validColl = db.books.validate();

//printjson(validColl);
if(!validColl.valid)
{
    db.createCollection("books", 
    {
        validator: 
        {
            $jsonSchema: 
            {
                bsonType: "object",
                required: [ "isbn", "title", "authors", "editor" ],
                properties: 
                {
                    isbn: {
                        bsonType: "string",
                        description: ""
                    },
                    title:
                    {
                        bsonType: "string",
                        description: ""
                    },
                    authors:
                    {
                        bsonType: "array",
                        items: 
                        {
                            bsonType: "objectId",
                            description: ""
                        }
                    },
                    editor:
                    {
                        bsonType: "objectId",
                        description: ""
                    },
                    releaseDate:
                    {
                        bsonType: "date",
                        description: ""
                    }
                }
            }
        }
    });

    db.books.createIndex({ "isbn": 1 }, { unique: true });

    print("Collection 'books' a été créé!")
} else {
    print("Collection 'books' existe déjà!")
}

//---------------------------------------------------------------------

//authors :
//- required : firstname, lastname
//- properties : firstname: string, lastname: string, birthdate: date, books [ObjectID]

var validColl = db.authors.validate();

//printjson(validColl);
if(!validColl.valid)
{
    db.createCollection("authors", 
    {
        validator: 
        {
            $jsonSchema: 
            {
                bsonType: "object",
                required: [ "firstname", "lastname"],
                properties: 
                {
                    firstname: {
                        bsonType: "string",
                        description: ""
                    },
                    lastname:
                    {
                        bsonType: "string",
                        description: ""
                    },
                    birthdate:
                    {
                        bsonType: "date",
                        description: ""
                    },
                    books:
                    {
                        bsonType: "array",
                        items:
                        {
                            bsonType: "objectId",
                            description: ""
                        }
                    }
                }
            }
        }
    });

    print("Collection 'authors' a été créé!")

} else {
    print("Colelction 'authors' existe déja!")
}

var authors = db.authors;
var editors = db.editors;
var books = db.books;

if(authors.countDocuments({}) == 0)
{
    print("initialize authors");
    authors.insertMany([
        // MONTH ARE 0 indexd !!! jan = 0, feb = 1, ... dec = 11
        {firstname: "Paolo", lastname: "Coalo", birthdate: new Date(1910, 0, 1), books: []},
        {firstname: "Victor", lastname: "Hugo", birthdate: new Date(1910, 1, 1), books: []},
        {firstname: "Mark", lastname: "Weber", birthdate: new Date(1910, 2, 1), books: []},
        {firstname: "Bernad", lastname: "Henri", birthdate: new Date(1910, 3, 1), books: []}
    ]);
}

if(editors.countDocuments({}) == 0)
{
    print("initialize editors");
    editors.insertMany([
        {NbrTVA: "abc123", name: "Nicolas Blanchard", creationDate: new Date(), books: []},
        {NbrTVA: "abc12", name: "Harper Colins", creationDate: new Date(), books: []},
        {NbrTVA: "abc1", name: "GAMBIT", creationDate: new Date(), books: []},
        {NbrTVA: "abc15", name: "la belle lettre", creationDate: new Date(), books: []}
    ]);
}

if(books.countDocuments({}) == 0)
{
    print("initialize books");
    
    var coalo = authors.findOne({lastname: 'Coalo'});
    var hugo = authors.findOne({lastname: 'Hugo'});
    var weber = authors.findOne({lastname: 'Weber'});
    var henri = authors.findOne({lastname: 'Henri'});

    var nicolasblanchard = editors.findOne({name : 'Nicolas Blanchard'});
    var harpercolins = editors.findOne({name : 'Harper Colins'});
    var gambit = editors.findOne({name : 'GAMBIT'});
    var labellelettre = editors.findOne({name : 'la belle lettre'});

    books.insertMany([
        { isbn: "12345", title: "alchemiste", releaseDate: new Date(), authors: [ coalo._id ], editor: nicolasblanchard._id},
        { isbn: "23456", title: "brazil", releaseDate: new Date(), authors: [ coalo._id ], editor: nicolasblanchard._id},
        { isbn: "34567", title: "les miserables", releaseDate: new Date(), authors: [ hugo._id ], editor: harpercolins._id},
        { isbn: "456789", title: "le soleil", releaseDate: new Date(), authors: [ weber._id ], editor: gambit._id},
        { isbn: "567890", title: "la lune", releaseDate: new Date(), authors: [ henri._id ], editor: labellelettre._id},
    ]);

    var alchemiste = books.findOne({isbn: "12345"});
    var brazil = books.findOne({isbn: "23456"});
    var lesmiserables = books.findOne({isbn: "34567"});
    var lesoleil = books.findOne({isbn: "456789"});
    var lalune = books.findOne({isbn: "567890"});

    coalo.books.push(alchemiste._id);
    coalo.books.push(brazil._id);
    hugo.books.push(lesmiserables._id);
    weber.books.push(lesoleil._id);
    henri.books.push(lalune._id);

    authors.updateOne({_id: coalo._id}, {$set: coalo});
    authors.updateOne({_id: hugo._id}, {$set: hugo});
    authors.updateOne({_id: weber._id}, {$set: weber});
    authors.updateOne({_id: henri._id}, {$set: henri});

    nicolasblanchard.books.push(alchemiste._id);
    nicolasblanchard.books.push(brazil._id);
    harpercolins.books.push(lesmiserables._id);
    gambit.books.push(lesoleil._id);
    labellelettre.books.push(lalune._id);

    editors.updateOne({_id: nicolasblanchard._id}, {$set: nicolasblanchard});
    editors.updateOne({_id: harpercolins._id}, {$set: harpercolins});
    editors.updateOne({_id: gambit._id}, {$set: gambit});
    editors.updateOne({_id: labellelettre._id}, {$set: labellelettre});
    

}

print('EDITORS')
printjson(editors.aggregate([{
    $lookup:
    {
        from: "books",
        localField: "books",
        foreignField: "_id",
        as: "books"
    }
}])._batch);

print('BOOKS')
printjson(books.aggregate([
    {
        $lookup:
        {
            from: "authors",
            localField: "authors",
            foreignField: "_id",
            as: "authors"
        }
    },
    {
        $lookup:
        {
            from: "editors",
            localField: "editor",
            foreignField: "_id",
            as: "editor"
        }
    },
    {
        $match: {title: "alchemiste"}
    }
])._batch);

print('AUTHORS')
printjson(authors.aggregate([
    { $match : { lastname: "Coalo"}},
    {
        $lookup:
        {
            from: "books",
            localField: "books",
            foreignField: "_id",
            as: "books"
        }
    },
    { $unwind: "$books"}
])._batch)

