from pydantic import BaseModel, field_validator

class PortfolioBlog(BaseModel):
    blog_id: int
    blog_title: str
    blog_date: str
    blog_abstract: str
    blog_markdown: str
    blog_image: str
    blog_image_source: str
    tag_id: int

    @field_validator('blog_title')
    @classmethod
    def blog_title_validation(cls, value:str)->str:
        return value.title()
    
    @field_validator('blog_image')
    @classmethod
    def blog_image_validation(cls, value:str)->str:
        if value.startswith("/assets/") and value.endswith("cover.png"):
                return value
        else:
            raise ValueError("Image is not dashyfied (start `/assets/` and ends `cover.png`):\n%s"%(value))
    
    @field_validator('blog_image_source')
    @classmethod
    def blog_image_source_validation(cls, value:str)->str:
        if value.startswith("http") or value.startswith("@"):
            return value
        else:
            raise ValueError("Image source is not http: %s"%(value[:5]))
    
    def to_dataframe(self):
        from pandas import DataFrame
        data = self.model_dump()
        df = DataFrame(
            [data], 
            columns=data.keys()
        ).astype(
            {
                "blog_id":"int",
                "blog_title":"str",
                "blog_date":"datetime64[ns]",
                "blog_abstract":"str",
                "blog_markdown":"str",
                "blog_image":"str",
                "blog_image_source":"str",
                "tag_id":"int"
            }
        )
        return df

    