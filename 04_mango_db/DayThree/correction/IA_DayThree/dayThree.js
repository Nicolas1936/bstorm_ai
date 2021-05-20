var db = db.getSiblingDB('DayThree');

db.editors.drop();
db.authors.drop();
db.books.drop();

var validColl = db.editors.validate();

printjson(validColl);

if(!validColl.valid)
{
    print("create collection: editors");
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
} else 
{
    print("collection \"editors\" already exist");
}

validColl = db.books.validate();

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
                    isbn: 
                    {
                        bsonType: "string",
                        description: ""
                    },
                    title: 
                    {
                        bsonType: "string",
                        description: ""
                    },
                    releaseDate: 
                    {
                        bsonType: "date",
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
                    }
                }
            }
        }
    });

    db.books.createIndex({ isbn: 1 }, { unique: true });
}

validColl = db.authors.validate();

if(!validColl.valid)
{
    db.createCollection("authors",
    {
        validator: 
        {
            $jsonSchema: 
            {
                bsonType: "object",
                required: [ "firstname", "lastname" ],
                properties:
                {
                    firstname: 
                    {
                        bsonType: "string",
                        description: ""
                    },
                    lastname: 
                    {
                        bsonType: "string",
                        description: ""
                    },
                    bithdate: 
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
}

var authors = db.authors;
var editors = db.editors;
var books = db.books;

if(authors.countDocuments({}) == 0)
{
    print("initialize authors");
    authors.insertMany([
        // MONTHS ARE 0 indexed !!! jan = 0, feb = 1, ... dec = 11
        { firstname: "John Ronald Reuel", lastname: "Tolkien", birthdate: new Date(1892, 0, 3), books: [] },
        { firstname: "Bertrand", lastname: "Russell", birthdate: new Date(1872, 4, 18), books: [] },
        { firstname: "John", lastname: "Nunn", birthdate: new Date(1955, 3, 18), books: [] },
        { firstname: "Lazlo", lastname: "Polgar", birthdate: new Date(1946, 4, 11), books: [] }
    ]);
}

if(editors.countDocuments({}) == 0)
{
    print("initialize editors");
    editors.insertMany([
        { NbrTVA: "abc123", name: "Harper Collins", creationDate: new Date(), books: [] },
        { NbrTVA: "abc124", name: "Black Dog & Leventhal", creationDate: new Date(), books: [] },
        { NbrTVA: "abc125", name: "GAMBIT", creationDate: new Date(), books: [] },
        { NbrTVA: "abc127", name: "Les Belles Lettres", creationDate: new Date(), books: [] }
    ]);
}

if(books.countDocuments({}) == 0)
{
    print("initialize books");

    var tolkien = authors.findOne({ lastname: "Tolkien" });
    var russell = authors.findOne({ lastname: "Russell" });
    var nunn = authors.findOne({ lastname: "Nunn" });
    var polgar = authors.findOne({ lastname: "Polgar" });

    var harperCollins = editors.findOne({ name: "Harper Collins"});
    var BDL = editors.findOne({ name: "Black Dog & Leventhal" });
    var gambit = editors.findOne({ name: "GAMBIT" });
    var lbl = editors.findOne({ name: "Les Belles Lettres"});

    books.insertMany([
        { isbn: "123456", title: "Lord of the Ring", releaseDate: new Date(), authors: [ tolkien._id ], editor: harperCollins._id },
        { isbn: "456789", title: "The Silmarillion", releaseDate: new Date(), authors: [ tolkien._id ], editor: harperCollins._id },
        { isbn: "123789", title: "Beren and Luthien", releaseDate: new Date(), authors: [ tolkien._id ], editor: harperCollins._id },
        { isbn: "789456", title: "Chess 5334 problems, combination, and games", releaseDate: new Date(), authors: [ polgar._id ], editor: BDL._id },
        { isbn: "456123", title: "John Nunn's chess puzzle book", releaseDate: new Date(), authors: [ nunn._id ], editor: gambit._id },
        { isbn: "654321", title: "Histoire de la philisophie occidentale", releaseDate: new Date(), authors: [ russell._id ], editor: lbl._id }
    ]);

    var lotr = books.findOne({ isbn: "123456" });
    var silmarillion = books.findOne({ isbn: "456789" });
    var berenAndLuthien = books.findOne({ isbn: "123789" });
    var ChessProblem = books.findOne({ isbn: "789456" });
    var johnNunnPuzzle = books.findOne({ isbn: "456123" });
    var histoireDeLaPhilo = books.findOne({ isbn: "654321" });

    tolkien.books.push(lotr._id);
    tolkien.books.push(silmarillion._id);
    tolkien.books.push(berenAndLuthien._id);
    polgar.books.push(ChessProblem._id);
    nunn.books.push(johnNunnPuzzle._id);
    russell.books.push(histoireDeLaPhilo._id);

    authors.updateOne({ _id: tolkien._id }, { $set: tolkien });
    authors.updateOne({ _id: polgar._id }, { $set: polgar });
    authors.updateOne({ _id: nunn._id }, { $set: nunn });
    authors.updateOne({ _id: russell._id }, { $set: russell });

    harperCollins.books.push(lotr._id);
    harperCollins.books.push(silmarillion._id);
    harperCollins.books.push(berenAndLuthien._id);
    BDL.books.push(ChessProblem._id);
    gambit.books.push(johnNunnPuzzle._id);
    lbl.books.push(histoireDeLaPhilo._id);

    editors.updateOne({ _id: harperCollins._id }, { $set: harperCollins });
    editors.updateOne({ _id: BDL._id }, { $set: BDL });
    editors.updateOne({ _id: gambit._id }, { $set: gambit });
    editors.updateOne({ _id: lbl._id }, { $set: lbl });
}

print("\n\tLOOKUP:")
printjson(authors.aggregate([{
    $lookup:
    {
        from: "books",
        localField: "books",
        foreignField: "_id",
        as: "books"
    }
}])._batch);

print("\n\tTWO LOOKUP")
printjson(books.aggregate([
    {
        $match: { title: "Lord of the Ring" }
    },
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
    }
])._batch);

print("\n\tUNWIND: ");
printjson(authors.aggregate([
    { $match: { lastname: "Tolkien" }},
    { $lookup: 
        {
            from: "books",
            localField: "books",
            foreignField: "_id",
            as: "books"
        }
    },
    { $unwind: "$books" }
])._batch);